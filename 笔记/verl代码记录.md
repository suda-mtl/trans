verl.trainer.main_ppo
RewardManager类：管理规则奖励
具体的奖励在verl\utils\reward_score\gsm8k.py里改

rollout过程
verl\workers\rollout\vllm_rollout\vllm_rollout_spmd.py

框架使用主要是两个点
1 自定义奖励 接收模型输入和模型输出和ground truth，根据规则给出数值奖励
2 外部工具调用：模型输出代码，外部解析器执行

明天做一个大笔记

RayPPOTrainer
## 准备数据
RayPPOTrainer._create_dataloader
计算训练轮数
total_training_steps = len(self.train_dataloader) * self.config.trainer.total_epochs

## 主训练循环
for epoch in range(self.config.trainer.total_epochs):
### rollout
gen_batch_output = self.actor_rollout_wg.generate_sequences(gen_batch)
1. verl/workers/fsdp_workers.py/ActorRolloutRefWorker.generate_sequences(self, prompts: DataProto) ->
2. verl/workers/rollout/vllm_rollout/vllm_rollout_spmd.py vLLMRollout.generate_sequences(self, prompts: DataProto) ->
3. response, tool_output_masks, execution_passes = self._tir_generate(
                prompts=vllm_inputs,  # because we have already convert it to prompt token id
                sampling_params=self.sampling_params,
                use_tqdm=False)
```python
# 设置vllm的停止词
sampling_params.stop=["```output"]
# 对话循环开始
while num_llm_calls_available >= 0:
    num_llm_calls_available-=1
    # 获取输入准备
    input_prompts, indices=self._get_prompts_and_indices(samples_info)
    # llm单步推理
    outputs = self.inference_engine.generate(prompts=input_prompts, sampling_params=sampling_params, use_tqdm=use_tqdm)
    # vllm的返回
    responses=[x.outputs[0].text for x in sorted_outputs]
    finish_reason=[x.outputs[0].finish_reason for x in sorted_outputs]
    stop_reason=[x.outputs[0].stop_reason for x in sorted_outputs]
    # 判断每个输出是否需要执行python代码
    is_execution=[_python_execution(finish_reason[i], stop_reason[i]) for i in range(len(finish_reason))]
    # 丛输出中提取代码
    tool_infos=[ _detect_tool(response) for response in responses]
    # 获取代码的执行结果
    observations=self.code_interpreter_batch_call([json5.loads(x)['code'] for x in tool_inputs])
    # 如果判断代码成功执行，将结果拼接到上一轮输出之后
    responses_w_res[index]+=processed_observation[0]
```
### rollout之后
将rollout的结果和输入拼接
batch = batch.repeat(repeat_times=self.config.actor_rollout_ref.rollout.n, interleave=True)
batch = batch.union(gen_batch_output)

计算old prob
old_log_prob = self.actor_rollout_wg.compute_log_prob(batch)

计算ref prob
ref_log_prob = self.ref_policy_wg.compute_ref_log_prob(batch)

计算基于规则的奖励
reward_tensor = self.reward_fn(batch)

判断是否加入KL散度
```python
if not self.config.actor_rollout_ref.actor.get('use_kl_loss', False):
    batch, kl_metrics = apply_kl_penalty(batch,
                                        kl_ctrl=self.kl_ctrl,
                                        kl_penalty=self.config.algorithm.kl_penalty)
    metrics.update(kl_metrics)
    else:
        batch.batch['token_level_rewards'] = batch.batch['token_level_scores']
```

计算优势
```python
batch = compute_advantage(batch,
                        adv_estimator=self.config.algorithm.adv_estimator,
                        gamma=self.config.algorithm.gamma,
                        lam=self.config.algorithm.lam,
                        num_repeat=self.config.actor_rollout_ref.rollout.n)
```

更新actor模型
```python
with _timer('update_actor', timing_raw):
            actor_output = self.actor_rollout_wg.update_actor(batch)
```

明天deepresearch 和 整理自己现在有什么技能？或方法？
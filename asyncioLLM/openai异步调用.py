import asyncio
from itertools import product
from openai import AsyncOpenAI
import os

# 单个api key
# 设置 OpenAI 客户端
api_key = "sk-67b47bbff8134add99108d538629f886"
base_url = "https://api.deepseek.com"  # 可选，例如使用本地模型服务时

client = AsyncOpenAI(api_key=api_key, base_url=base_url)

# 输入数据
nums1 = [1545, 5643]
nums2 = [124]

# 提示模板
PROMPT_TEMPLATE = "请计算{}*{},给出完整的计算过程"

# 创建信号量，限制最大并发数为 10
SEMAPHORE = asyncio.Semaphore(10)

async def multiply_with_llm(a: int, b: int) -> str:
    prompt = PROMPT_TEMPLATE.format(a, b)
    response = await client.chat.completions.create(
                model="deepseek-chat",  # 替换为你实际可用的模型
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=1000,
            )
    return response.choices[0].message.content
    # async with SEMAPHORE:  # 限制并发
    #     try:
    #         response = await client.chat.completions.create(
    #             model="deepseek-chat",  # 替换为你实际可用的模型
    #             messages=[{"role": "user", "content": prompt}],
    #             temperature=0.0,
    #             max_tokens=500,
    #         )
    #         return response.choices[0].message.content
    #     except Exception as e:
    #         return f"Error for {a} * {b}: {str(e)}\n{'-'*50}"

async def main():
    tasks = []
    for a, b in product(nums1, nums2):
        task = multiply_with_llm(a, b)
        tasks.append(task)

    print(f"共需执行 {len(tasks)} 个乘法任务，最多并发 10 个...\n")

    results = await asyncio.gather(*tasks)

    # 按顺序输出结果（可选：也可在任务完成时实时打印）
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
    
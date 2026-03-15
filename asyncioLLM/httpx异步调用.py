import asyncio
from itertools import product
import os
import httpx

# 配置（根据你使用的后端修改）
api_key = ""
base_url = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"  # 替换为你本地加载的模型名

# 输入数据
nums1 = [1545, 5643, 472, 871, 16545]
nums2 = [124, 3578, 2356, 2311]

PROMPT_TEMPLATE = "请计算{}*{},给出完整的计算过程"

# 创建带并发限制的信号量
SEMAPHORE = asyncio.Semaphore(20)

async def multiply_with_llm(a: int, b: int, client: httpx.AsyncClient) -> str:
    prompt = PROMPT_TEMPLATE.format(a, b)
    url = f"{base_url.rstrip('/')}/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": 500,
    }

    async with SEMAPHORE:
        try:
            response = await client.post(url, json=payload, headers=headers, timeout=60.0)
            response.raise_for_status()
            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
            return f"{a} * {b}:\n{content}\n{'-'*50}"
        except Exception as e:
            return f"Error for {a} * {b}: {type(e).__name__}: {e}\n{'-'*50}"

async def main():
    # 共享一个 AsyncClient（复用连接，提升性能）
    async with httpx.AsyncClient() as client:
        tasks = []
        for a, b in product(nums1, nums2):
            task = multiply_with_llm(a, b, client)
            tasks.append(task)

        print(f"共需执行 {len(tasks)} 个任务，最多并发 20 个...\n")
        results = await asyncio.gather(*tasks)

        for res in results:
            print(res)

if __name__ == "__main__":
    asyncio.run(main())

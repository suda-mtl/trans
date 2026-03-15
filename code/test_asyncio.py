import asyncio
import time


async def async_hello_world(i):
    # now = time.time()
    # await time.sleep(1)
    await asyncio.sleep(i*5)
    print(f'1 current {i}', time.time() - now)
    print("Hello, world!")
    with open(f'./{i}.txt', 'w', encoding='utf-8') as f:
        f.write(f"Hello, world!{i}")
    # await asyncio.sleep(1)
    # print(f'2 current {i}', time.time() - now)
    return i

async def main():
    tasks=[]
    for i in range(1, 4):
        tasks.append(async_hello_world(i))
    results= await asyncio.gather(*tasks)
    print('results', results)
    print(type(results))
    # await asyncio.gather(async_hello_world(), async_hello_world(), async_hello_world())

now = time.time()
# run 3 async_hello_world() coroutine concurrently
asyncio.run(main())

print(f"Total time for running 3 coroutine: {time.time() - now}")

import time
def normal_hello_world():
    # now = time.time()
    time.sleep(1)
    print(time.time() - now)
    print("Hello, world!")
    time.sleep(1)
    print(time.time() - now)

# now = time.time()
# normal_hello_world()
# normal_hello_world()
# normal_hello_world()
# print(f"Total time for running 3 normal function: {time.time() - now}")
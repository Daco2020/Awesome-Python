import aiohttp  # aiohttp~=3.7.3 버전 사용
import asyncio
import requests
import time


async def success(num):
    # time.sleep(2)
    await asyncio.sleep(2)
    return num * 10000


async def main():
    result = await asyncio.gather(*[success(i) for i in range(5)])
    print(result)
    print('바나나')


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)

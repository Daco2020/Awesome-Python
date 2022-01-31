'''
동기로 코드를 작성할 경우
15.04025387763977 초 소요
'''

import aiohttp  # aiohttp~=3.7.3 버전 사용
import asyncio
import requests
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://daum.net"] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

# >>> 15.04025387763977 초


'''
코루틴을 활용하여 비동기로 코드를 작성할 경우(약 10배 더 빠른 처리속도를 보여준다)
1.7667789459228516 초 소요
'''


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://daum.net"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)

# >>> 1.7667789459228516 초

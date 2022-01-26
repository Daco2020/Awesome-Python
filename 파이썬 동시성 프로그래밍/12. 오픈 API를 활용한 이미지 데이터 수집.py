'''
- 네이버 api를 활용하여 이미지 크롤링하기
- config 파일에 api id와 secret을 따로 빼어 해당 정보가 공개되지 않도록 관리함
- 코드는 동시성으로 작동함
'''

import aiohttp
import asyncio
from config import naver_api_header


async def fetch(session, url, i):
    print(i + 1)
    async with session.get(url, headers=naver_api_header) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        print(images)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    query = "지지율"
    display = 10
    urls = [
        f"{BASE_URL}?query={query}&display={display}&start={i}" for i in range(1, 10)
    ]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())

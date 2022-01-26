'''
pip install aiofiles==0.7.0
---
이미지에 대한 session을 추가로 불러온다.
    session은 요청을 보내는 객체?라고 보면 될 거 같다.

aiofiles를 이용하여 이미지들을 파일로 저장한다.
    파일명은 날짜시간으로 변경하여 저장한다.
*aiofiles를 사용하는 이유는?
    비동기 방식으로 프로그래밍을 하려면 이미 비동기로 만들어진 함수를 잘 활용 해야 한다. 
    비동기 파일 입출력은 aiofiles라는 라이브러리를 이용하여 처리할 수 있다.
    레퍼런스 : https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D

'''

import os
import aiohttp
import asyncio
from config import naver_api_header
import aiofiles
from datetime import datetime


async def img_downloader(session, img):
    # img_name = img.split("/")[-1] # /를 기준으로 파일명 축소
    img_name = f"{datetime.today()}.jpg"  # 파일명을 날짜로 변경
    print(img_name)

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url, i):
    print(i + 1)
    async with session.get(url, headers=naver_api_header) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]

        # img_downloader로 session과 img링크 넘겨주기(jpg 파일만)
        await asyncio.gather(*[img_downloader(session, img) for img in images if ".jpg" in img])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "배고파"
    display = 10
    urls = [
        f"{BASE_URL}?query={keyword}&display={display}&start={i*display+1}" for i in range(5)
    ]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())

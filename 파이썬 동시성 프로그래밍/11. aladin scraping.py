'''
동시성을 활용한 알라딘 웹 크롤링
'''

from bs4 import BeautifulSoup
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        suop = BeautifulSoup(html, 'html.parser')
        names = suop.find_all("a", "bo3")
        for name in names:
            title = name.find("b")
            if title is not None:
                print(title.text)


async def main():
    BASE_URL = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&"
    urls = [
        # 페이지 번호에 따라 데이터를 가져오도록 작성함
        f"{BASE_URL}page={i}&Stockstatus=1&PublishDay=84&CID=3057&SearchOption=" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        # *는 리스트를 해체해 줌
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""

from bs4 import BeautifulSoup  # html 을 해석하여 그 안의 데이터를 가공하는 패키지임


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")  # soup 객체 만들기
# "html.parser"는 무엇인가?


print(soup.prettify())  # prettify() 매서드는 html을 예쁘게 가져온다

print(soup.title)  # 해당 html 페이지의 타이틀

print(soup.p)  # p 태그를 불러옴

print(soup.find("p", "title"))  # 첫번째 인자는 태그, 두번째 인자는 클래스명을 넣으면 해당 데이터를 가져온다.
print(soup.find("p", "story").text)  # text 매서드를 활용하면 해당 텍스트만 가져올 수 있다

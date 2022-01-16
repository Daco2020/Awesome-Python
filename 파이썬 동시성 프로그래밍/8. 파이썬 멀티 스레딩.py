import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
'''
concurrent.futures 모듈은 비동기적으로 콜러블을 실행하는 고수준 인터페이스를 제공합니다.
비동기 실행은 (ThreadPoolExecutor를 사용해서) 스레드나 (ProcessPoolExecutor를 사용해서) 별도의 프로세스로 수행 할 수 있습니다.
'''


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")

    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com"] * 5

    # max_workers=? 작업할 스레드의 수를 지정
    # 1개 지정시 1.9초
    # 10개 지정시 0.5초
    executor = ThreadPoolExecutor(max_workers=1)

    with requests.Session() as session:

        # 인수가 여러개이므로 리스트로 만든다
        params = [(session, url) for url in urls]

        # map 매서드, 함수와 인수를 넣는다
        # map은 재너레이터 객체이기 때문에 리스트로 바꿔준다
        list(executor.map(fetcher, params))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)


'''
기존 실습 코드에서 어떤 프로세스와 스레드가 사용되는지 확인해보자

`print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")`
`os.getpid()` : 현재 **프로세스 아이디(PID)**를 반환한다
`threading.get_ident()` : 현재 **스레드의 식별자**를 반환한다


멀티 스레드의 결과 값

```bash
# ThreadPoolExecutor(max_workers=10) 의 경우
# 스레드 식별자가 모두 다른 것을 볼 수 있다 -> 멀티 스레드

69503 process | 12953890816 url : https://naver.com
69503 process | 12970680320 url : https://google.com
69503 process | 12987469824 url : https://naver.com
69503 process | 13004259328 url : https://google.com
69503 process | 13021048832 url : https://naver.com
69503 process | 13037838336 url : https://google.com
69503 process | 13054627840 url : https://naver.com
69503 process | 13071417344 url : https://google.com
69503 process | 13088206848 url : https://naver.com
69503 process | 13104996352 url : https://google.com
0.5615730285644531
```

싱글 스레드의 결과 값

```bash
# ThreadPoolExecutor(max_workers=1) 의 경우
# 스레드 식별자가 모두 같은 것을 볼 수 있다 -> 싱글 스레드

69522 process | 13074235392 url : https://naver.com
69522 process | 13074235392 url : https://google.com
69522 process | 13074235392 url : https://naver.com
69522 process | 13074235392 url : https://google.com
69522 process | 13074235392 url : https://naver.com
69522 process | 13074235392 url : https://google.com
69522 process | 13074235392 url : https://naver.com
69522 process | 13074235392 url : https://google.com
69522 process | 13074235392 url : https://naver.com
69522 process | 13074235392 url : https://google.com
1.9546759128570557
```

스레드를 만들고 우선순위를 부여하는 것도 모두 연산과정이며 메모리 점유율이 높아진다. 
그래서 asyncio로 코루틴으로 동작하는 것이 스레드를 추가하는 것보다 더 효율이 좋다

레퍼런스

- [concurrent.futures](https://docs.python.org/ko/3.8/library/concurrent.futures.html?highlight=threadpoolexecutor)
'''

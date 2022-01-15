'''
CPU 바운드
연산을 많이 해서 cpu가 막는 행위
프로그램이 실행될 때 실행 속도가 cpu 속도에 의해 제한됨을 의미함
정말 복잡한 수학 수식을 계산하는 경우에 컴퓨터의 실행속도가 느려진다


I/O 바운드
I는 인풋, O는 아웃풋
프로그램이 실행될 때 실행 속도가 I/O에 의해 제한됨을 의미함
사용자가 입력을 해야 다음 단계가 진행되는 경우
네트워크 I/O : 컴퓨터와 컴퓨터끼리 통신을 할 때
블로킹 : 바운드에 의해 코드가 멈추게 되는 현상



실습 코드 : 구글에 요청을 반복한다면?
pip3 install requests

---
import requests


def func():
    ‌result = requests.get("<https://google.com>")
    ‌return result


for i in range(10):
    ‌result = func()

print(result)
---



요청과 응답을 기다리는 과정에서
코드가 멈추게 되는 현상을 바운드라고 한다
위의 코드는 짧긴 하지만 블로킹 10회가 일어난 것이다
'''

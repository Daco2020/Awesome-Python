'''
루틴이란?
일련의 명령 흐름 (코드의 흐름)



메인 루틴
프로그램의 메인 코드의 흐름



서브 루틴 ( = 함수 )
함수나 메서드 (메인 루틴을 보조하는 역할)
하나의 진입점과 하나의 탈출점이 있는 루틴



코루틴
서브루틴의 일반화된 형태
다양한 진입점과 다양한 탈출점이 있는 루틴
    await에 의해 진입과 탈출점이 추가됨
    비동기적 코드를 가능하게 함

await 은 어웨이터블 객체 앞에 사용한다
어웨이터블 객체는 코루틴, 태스크 및 퓨처를 의미한다

    코루틴 함수
        time.sleep() → X
        asyncio.sleep() → O
        함수 정의 시 async 를 붙이는 경우 → O

    태스크 객체
        태스크를 예약할 때 사용
        task1 = asyncio.create_task(func())
        await task1 # 이렇식으로 코드 실행

    퓨처
        저수준 어웨이터블 객체 → 다음에 자세히




코루틴 기본 문법
asyncio.run(func())
    코루틴 실행하는 매소드

asyncio.sleep([second])
    코루틴 실행을 지연하는 매소드

asyncio.gather(func())
    동시에 태스크 실행하기
    리턴 값은 리스트 형태로 반환한다
    동시성(컨커런시)으로 실행된다
    병렬성은 아니다


---
# 코루틴 실습 코드

import asyncio

async def func():
‌print("hello")
‌# await print("hello") 이렇게는 사용불가. awaitable 하지 못하기 때문

if __name__ == "__main__":
‌# asyncio에 인자로 함수로 넣으면 코루틴으로 실행할 수 있다
‌asyncio.run(func()) 
---

'''

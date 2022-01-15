'''
동기란?
코드가 반드시 작성된 순서로 실행된다
요청 후 응답을 받지 못하면 바운드 상태를 유지한다
이전 요청에 대한 응답을 받아야만 다음 코드를 진행하므로 연산이 느려진다
예) 주문 받은 순서대로 처리한다. 앞선 주문이 완료되지 않으면 다음 주문으로 넘어가지 않는다


비동기란?
코드가 반드시 작성된 순서로 실행되는 것이 아니다
요청 후 응답을 받지 못해도 바운드 없이 다음 코드를 수행한다
이전 요청에 대한 응답을 기다리지 않으므로 동기보다 더 빠르게 연산이 가능하다
예) 주문을 수행하지만 완료되지 않아도 다음 주문을 진행한다


무조건 비동기가 좋을까?
단순한 계산은 비동기로 구현할 경우 코드가 복잡해지고 유지보수가 어려워질 수 있다
다음 단계로 넘어가면 안되는 계산이라면 동기로 구현하자


동기 비동기 비교를 위한 시간 측정 코드

time.time() 현재 시간을 체크하는 코드
time.sleep([초]) 인수로 넣은 초만큼 코드를 지연시키는 코드 


---
import time

start = time.time()
''
수행할 코드
''
end = time.time()
---

'''

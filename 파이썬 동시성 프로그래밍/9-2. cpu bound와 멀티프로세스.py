import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

nums = [30] * 100
# 멀티스레딩 22초 <> 멀티프로세싱 13초
# 멀티스레딩은 cpu_bound 에서 의미가 없다. 오히려 더 느려진다.


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


# # 일반 18초, 컴프리핸션 18초, 프린트 36초
# def main():
#     results = [cpu_bound_func(num) for num in nums]
#     print(results)


# 멀티 프로세싱 33초(3초 단축) +(nums 수정 후)
def main():
    executor = ProcessPoolExecutor(max_workers=10)
    result = list(executor.map(cpu_bound_func, nums))
    print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 일반

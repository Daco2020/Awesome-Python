from concurrent.futures import ThreadPoolExecutor
import time
import os
import threading

nums = [30] * 100
# 22초


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


# 멀티 스레딩 18초, 프린트 36초 -> cpu bound 의 경우 멀티스레딩의 의미가 없다.
def main():
    executor = ThreadPoolExecutor(max_workers=10)
    result = list(executor.map(cpu_bound_func, nums))
    print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

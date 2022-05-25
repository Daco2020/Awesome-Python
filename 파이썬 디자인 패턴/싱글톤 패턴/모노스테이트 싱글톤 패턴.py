class Mono:
    __shared_state = {"공유":"데이터"}
    def __init__(self):
        self.data = 1
        self.__dict__ = self.__shared_state
        pass

obj = Mono()
obj.data = 9999
other_obj = Mono()

print(f"{obj=}")
print(f"{other_obj=}")
"""
결과값. 서로 다른 인스턴스임을 확인할 수 있음
obj=<__main__.Mono object at 0x1011ffb50>
other_obj=<__main__.Mono object at 0x101477790>
"""

print(f"{obj.__dict__=}")
print(f"{other_obj.__dict__=}")
"""
결과값. 서로 다른 인스턴스지만 상태는 공유하고 있다. 
obj.__dict__={'공유': '데이터', 'data': 9999}
other_obj.__dict__={'공유': '데이터', 'data': 9999}
"""

"""
만약 'self.__dict__ = self.__shared_state' 를 하지 않는다면,
다음처럼 인스턴스 끼리 상태를 공유하지 못한다.

결과값.
obj.__dict__={'data': 9999}
other_obj.__dict__={'data': 1}
"""

# ----------
# __new__ 로 구현 하는 방법

class Mono(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Mono, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

obj = Mono()
obj.data = 9999
other_obj = Mono()

print(f"{obj=}")
print(f"{other_obj=}")
"""
결과값. 서로 다른 인스턴스임을 확인할 수 있음
obj=<__main__.Mono object at 0x100ed3730>
other_obj=<__main__.Mono object at 0x100ed3700>
"""

print(f"{obj.__dict__=}")
print(f"{other_obj.__dict__=}")
"""
결과값. 서로 다른 인스턴스지만 상태는 공유하고 있다. 
obj.__dict__={'data': 9999}
other_obj.__dict__={'data': 9999}
"""
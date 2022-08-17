# from abc import ABC, abstractmethod
from typing import Protocol


class 감정(Protocol):
    def 기쁘다(self) -> str:
        ...

    def 슬프다(self) -> str:
        ...


class 이성(Protocol):
    def 맞다(self) -> str:
        ...

    def 틀리다(self) -> str:
        ...


class 사람:
    def 기쁘다(self) -> str:
        return "기뻐!"

    def 슬프다(self) -> str:
        return "슬퍼!"

    def 맞다(self) -> str:
        return "맞아!"

    def 틀리다(self) -> str:
        return "틀려!"


class 사회생활:
    def 시작(self, 사람: 이성) -> None:
        self.사람 = 사람

    def 기쁜일(self) -> str:
        return self.사람.기쁘다()

    def 틀린일(self) -> str:
        return self.사람.틀리다()


갓생 = 사회생활()
갓생.시작(사람())

print(갓생.기쁜일())
print(갓생.틀린일())


# class 감정2(ABC):
#     @abstractmethod
#     def 기쁘다(self) -> str:
#         ...


# class 사람2(감정2):
#     def 슬퍼(self) -> str:
#         return "추상적으로 슬퍼!"


# 나 = 사람2()
# print(나.슬퍼())


# from typing import Protocol


# class 감정(Protocol):
#     def 기쁘다(self) -> str:
#         ...

#     def 슬프다(self) -> str:
#         ...


# class 사람:
#     def 기쁘다(self) -> str:
#         return "기뻐!"

#     def 화나다(self) -> str:
#         return "화나!"


# class 사회생활:
#     def 시작(self, 사람: 감정) -> None:
#         self.사람 = 사람

#     def 기쁜일(self) -> str:
#         return self.사람.기쁘다()

#     def 화날일(self) -> str:
#         return self.사람.화나다()


# 갓생 = 사회생활()
# 갓생.시작(사람())

# print(갓생.기쁜일())
# print(갓생.화날일())

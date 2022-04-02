"""
#* [@property]를 사용하는 이유
#* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
#* 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class Robot:

    """
    Robot Class
    """

    __population = 0 # __를 붙이면 변수, 메서드, 등을 숨길 수 있다. 외부에서는 접근 불가, 내부에서는 접근 가능

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property # __로 숨긴 값을 불러오려면 프로퍼티 데코레이터를 붙여야 한다.
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.__age

    @age.setter # 프로퍼티한 함수를 가져와 setter를 붙인다.
    def age(self, new_age):
        if new_age - self.__age == 1: # 값이 수정될 경우 유효성 검사를 할 수 있다.
            self.__age = new_age
        else:
            raise ValueError()

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


droid = Robot("R2-D2", 2)


print(droid.age)

# droid.age = 7

droid.age += 1


print(droid.age)


print(droid.name)
import datetime

class Robot:
    
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")
        '''
        @classmethod가 지정되어 있어야 인자를 받지 않아도 실행가능.
        없다면 객체이든 클래스이든 인자를 넣어주어야 함.
        인스턴스와 상관없이 클래스 내에서 사용하는 함수
        '''

    # 스태틱 메서드
    @staticmethod
    def time():
        return f"The current time is {datetime.datetime.now()}."
        
siri = Robot('siri')

print(Robot.time())
'''
>>> The current time is 2022-03-31 13:12:10.531137.
'''


print(siri.time())
'''
>>> TypeError: time() takes 0 positional arguments but 1 was given
만약 @staticmethod을 하지 않으면 인스턴스로 호출시 오류가 뜸.

>>> The current time is 2022-03-31 13:12:10.531137.
정적 메서드로 바꾸어 주어야 클래스와 인스턴스 모두 호출 가능함.
객체와 상관없이 값을 반환해야하는 경우 사용가능.
'''
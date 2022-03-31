class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


droid1 = Robot("R2-D2")
droid1.say_hi()

print(dir(droid1))

print(droid1)  # <__main__.Robot object at 0x7fde1c742110> -> R2-D2 robot!!


droid1()

'''
함수() 옆에 () 는 callable 호출이 가능함을 말한다.
함수도 객체인데 일반 객체는 ()로 호출이 불가하다. 
그 이유는 함수안에는 __call__ 매직매서드가 있기 때문이다.
'''
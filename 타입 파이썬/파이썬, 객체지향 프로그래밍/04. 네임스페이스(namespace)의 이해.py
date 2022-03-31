"""
#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다.
#* dir() : 네임스페이스의 key 값을 확인할 수 있다.
#* __doc__ : class의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""
"""
객체의 네임스페이스에서는 변수만 확인 가능하다.(메서드x)
그렇다면 객체에서 메서드를 사용할 수 있는 이유는?
객체를 생성한 클래스를 찾아가 클래스 네임스페이스에 있는 메서드를 불러온다.
"""

class Robot:
    '''
    주석 테스트 
    '''

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


siri = Robot("siri")  # {'name': 'siri'}
jarvis = Robot("jarvis")
bixby = Robot("bixby")

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)

print(siri.name)
print(bixby.name)

siri.cal_add(2, 3)

# population는 클래스 변수이지만 인스턴스를 통해서도 접근할 수 있다.
# 여기서 population는 모든 객체가 공유하는 변수가 됨.
print(siri.population) 

# 같은 원리로 인스턴스도 클래스 메서드 사용가능
siri.how_many()


# say_hi는 인스턴스(self) 메서드이기 때문에 안에 인스턴스 객체를 넣어야 실행 가능
Robot.say_hi(siri)
siri.say_hi()


print(dir(siri))
print(dir(Robot))


print(Robot.__doc__)
# >>> 주석 테스트 



print(siri.__class__)
# >>> <class '__main__.Robot'>
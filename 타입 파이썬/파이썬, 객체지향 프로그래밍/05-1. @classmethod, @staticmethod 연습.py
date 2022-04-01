class Robot:
    number = '0001'
    
    def __init__(self, name):
        self.name = name
        
    def 인스턴스메서드(self):
        print(f'인스턴스메서드 호출 {self.name}')
        
    @classmethod
    def 클래스메서드(cls):
        print(f'클래스메서드 호출 {cls.number}')
    
    @staticmethod
    def 스태틱메서드():
        print('스태틱메서드 호출')
        
robot = Robot('다코')

# robot -> 인스턴스
# Robot -> 클래스


robot.인스턴스메서드()
Robot.인스턴스메서드()
'''
클래스가 일반 인스턴스메서드를 호출하면 아래와 같은 오류가 발생
TypeError: 인스턴스메서드() missing 1 required positional argument: 'self'
클래스가 인스턴스메서드를 사용하려면 인자로 객체를 넣어주어야 함
여기서는 Robot.인스턴스메서드(robot)

'''


robot.클래스메서드()
Robot.클래스메서드()
'''
@classmethod 를 설정하지 않으면 클래스로 호출 시 아래와 같은 오류가 발생
TypeError: 클래스메서드() missing 1 required positional argument: 'cls'
클래스가 클래스메서드를 사용하려면 인자로 클래스를 넣어주어야 함
여기서는 Robot.클래스메서드(Robot)
'''


robot.스태틱메서드()
Robot.스태틱메서드()
'''
@staticmethod 를 설정하지 않으면 인스턴스 호출 시 아래와 같은 오류가 발생
TypeError: 스태틱메서드() takes 0 positional arguments but 1 was given
인자를 넣지 않았음에도 인자가 있다는 오류.
이 경우에는 클래스의 인자를 비워두지 않고 self를 넣어야 함.
하지만 굳이 self가 필요하지 않고 클래스에서도 사용하기 위해 @staticmethod를 설정
'''

class Robot:
    def __init__(self, name, num):
        self.__name = name
        self._num = num
    
    def __call(self):
        print(f'이름: {self.__name}, 일련번호: {self._num}, 호출합니다.') # 외부에서는 부를 수 없지만, 내부에서는 부를 수 있음.
        
    def call_a_call(self):
        return self.__call()
    
    @property
    def name(self): # 함수명을 변수명과 일치시켜 변수에 접근하는 것처럼 구현
        return self.__name
    
    @name.setter 
    def name(self, new_name): # 함수명을 변수명과 일치시켜 변수에 접근하는 것처럼 구현
        if not type(new_name) == str:
            raise ValueError 
        self.__name = new_name
        return self.__name
    
robot = Robot('다코', '0001')

print(robot._Robot__name) # 사실 _클래스명 을 앞에 붙이면 접근할 수 있다. 완전한 캡슐화라 보기 어렵다.
print(robot.__name) # 외부에서는 접근할 수 없다.
# print(robot._num) # _는 __처럼 숨기지는 못하지만 숨긴다고 가정하는 표시이다.


# robot.call() # AttributeError: 'Robot' object has no attribute '__call'
# robot.__call() # AttributeError: 'Robot' object has no attribute '__call'
# robot.call_a_call() # 이름: 다코, 일련번호: 0001, 호출합니다.

print(robot.name) # >>> 다코, 외부에서 name으로 접근할 수 있다.
robot.name = '스누피' # setter가 없다면, >>> AttributeError: can't set attribute 에러 발생
print(robot.name) # >>> 스누피, 외부에서 name을 수정할 수 있다.

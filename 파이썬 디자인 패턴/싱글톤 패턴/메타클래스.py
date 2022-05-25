print(type(5)) # <class 'int'>
print(type(int)) # <class 'type'>
print(type(type(5))) # <class 'type'>

"""
숫자 5의 타입은 int이며, int의 타입은 type이다.
즉, 'type'은 'int'의 메타클래스이다.
"""


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances: # 인스턴스가 있으면 생성하지 않음
            cls._instances[cls] = super(MetaSingleton,\
                cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def show(slef): # 상속 확인용 메서드
        print("상속확인")
        

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
print(logger1 is logger2)

"""
결과값. 한 개의 인스턴스를 생성한다.
<__main__.Logger object at 0x1028f7e80> <__main__.Logger object at 0x1028f7e80>
True
"""

print(logger1.show()) 
"""
결과값. 메타클래스는 메서드 상속이 안됨
Traceback (most recent call last):
  File "*********", line 30, in <module>
    print(logger1.show())
AttributeError: 'Logger' object has no attribute 'show'
"""

class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)
    
    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__,":: Got", args, "From", subject)
    
class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__,":: Got", args, "From", subject)
    
subject = Subject()
Observer1(subject)
Observer2(subject)
subject.notifyAll("알림1","알림2")

"""
# 결과 값.
Observer1 :: Got ('알림1', '알림2') From <__main__.Subject object at 0x100f67e20>
Observer2 :: Got ('알림1', '알림2') From <__main__.Subject object at 0x100f67e20>
"""

"""
- 서브젝트 : 옵저버를 관리한다. 1대다 로서 서브젝트는 여러 옵저버를 관리한다.
- 옵저버 : 서브젝트를 감시하는 객체를 위한 인터페이스 제공
- 콘크리트 옵저버 : 서브젝트의 상태를 저장한다. 서브젝트에 대한 정보와 실제 상태를 일관되게 유지하도록 옵저버 인터페이스를 구현한다.
"""
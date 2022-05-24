class Singleton(object):
    # __new__를 오버라이드 한다.
    def __new__(cls):
        # hasattr는 객체가 instance 속성을 가지고 있는지 확인한다. (객체의 존재 유무 확인)
        if not hasattr(cls, 'instance'):
            # 클래스 객체가 없다면 객체를 할당한다.
            cls.instance = super(Singleton, cls).__new__(cls)
        # 기존 또는 할당한 객체를 반환한다.
        return cls.instance

obj = Singleton()
print("created", obj)

other_obj = Singleton()
print("created", other_obj)

"""
created <__main__.Singleton object at 0x101033640>
created <__main__.Singleton object at 0x101033640>
"""
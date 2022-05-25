class Singleton:
    __instance = None
    def __init__(self):
        # 인스턴스가 생성되지 않을 때 메시지
        if not Singleton.__instance:
            print("__init__ method called...")
        # 인스턴스가 생성되었을 때 메시지
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        # 인스턴스가 없다면 생성하는 메서드
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() # 인스턴스를 생성하지 않음
# __init__ method called...

print(f"{s=}") 
# s=<__main__.Singleton object at 0x100ca7610>

print("created", Singleton.getInstance()) # 인스턴스 생성
# __init__ method called...
# created <__main__.Singleton object at 0x100ca75e0>

s1 = Singleton() # 인스턴스가 이미 생성되었음
# Instance already created: <__main__.Singleton object at 0x100ca75e0
print(f"{s1=}")
# s1=<__main__.Singleton object at 0x100ca75b0> 

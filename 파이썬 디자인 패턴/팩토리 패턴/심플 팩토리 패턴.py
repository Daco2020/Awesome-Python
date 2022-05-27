from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("Warl Warl!!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


## 팩토리 클래스
class AnimalFactory(object):
    def make_sound(self, object_type): # Dog, Cat 문자열이 eval를 통해 Dog, Cat 클래스를 실행한다.
        return eval(object_type)().do_say() # eval사용법 : https://bio-info.tistory.com/84


## 클라이언트 코드
if __name__ == '__main__':
    factory = AnimalFactory()
    animal = input("어떤 동물을 선택하시겠습니까? (Dog or Cat)")
    factory.make_sound(animal)


"""
결과값 1.
어떤 동물을 선택하시겠습니까? (Dog or Cat)Cat
Meow Meow!!

결과값 2.
어떤 동물을 선택하시겠습니까? (Dog or Cat)Dog
Warl Warl!!
"""


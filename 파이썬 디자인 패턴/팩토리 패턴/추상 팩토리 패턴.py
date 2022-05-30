from abc import abstractmethod


# AbstractFactory
class PizzaFactory:
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass

# ConcreateFactory
class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()

class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


# AbstractPorduct
class VegPizza:
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza:
    @abstractmethod
    def serve(self, VegPizza):
        pass

# ConcreateProducts
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print(f"{type(self).__name__} 를 준비합니다.")

class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(f"{type(self).__name__} 는 {type(VegPizza).__name__} 에 치킨을 추가합니다.")

class MexicanVegPizza(VegPizza):
    def prepare(self):
        print(f"{type(self).__name__} 를 준비합니다.")

class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(f"{type(self).__name__} 는 {type(VegPizza).__name__} 에 햄을 추가합니다.")


# 실행 클래스
class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)
        
pizza = PizzaStore()
pizza.makePizzas()


"""
# 결과.
DeluxVeggiePizza 를 준비합니다.
ChickenPizza 는 DeluxVeggiePizza 에 치킨을 추가합니다.
MexicanVegPizza 를 준비합니다.
HamPizza 는 MexicanVegPizza 에 햄을 추가합니다.
"""
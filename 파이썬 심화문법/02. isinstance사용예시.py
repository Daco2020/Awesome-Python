'''
isinstance(object, classinfo)

객체 인수가 classinfo 인수 또는 (직접, 간접 또는 가상) 하위 클래스의 인스턴스인 경우 True를 반환합니다. 
객체가 주어진 유형의 객체가 아니면 함수는 항상 False를 반환합니다. 
classinfo가 유형 객체의 튜플(또는 재귀적으로, 다른 튜플)이거나 여러 유형의 Union Type이면 객체가 유형 중 하나의 인스턴스인 경우 True를 반환합니다. 
classinfo가 유형 또는 유형의 튜플 및 그러한 튜플이 아닌 경우 TypeError 예외가 발생합니다.
'''

def 체크_문자열(객체):
    return isinstance(객체, str)

def 체크_리스트(객체):
    return isinstance(객체, list)

print(체크_문자열('문자')) # >>> True
print(체크_문자열(123)) # >>> False

print(체크_리스트('문자')) # >>> False
print(체크_리스트(123)) # >>> False
print(체크_리스트([1,2,3])) # >>> True


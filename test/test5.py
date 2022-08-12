# class A:
#     def __init__(self):
#         self.a = "a"

#     @property
#     def get_b(self, c):
#         if c:
#             return "b"
#         else:
#             print("no")


# a = A()
# print(a)
# print(a.get_b)

from dataclasses import Field, dataclass, field, fields, is_dataclass
from typing import Literal, NewType, Type, TypedDict, _TypedDictMeta


class Typeddict(TypedDict):
    tag: Literal["typeddict"]
    a: str


@dataclass(frozen=True)
class Dataclass:
    a: int
    b: str


asd = Dataclass(a=1, b="s")
print([field.name for field in fields(asd)])


a = Typeddict

# print(type(Typeddict(a=1)) is Typeddict) # False
# print(type(Typeddict(a=1)) is dict)      # True
# print(type(Dataclass(a=1)) is Dataclass) # True

b = Typeddict(tag="a", a=1)

# print(type(b["tag"]))
# print(type(Typeddict))
# print(zxc)
# print(type(zxc))

# print(issubclass(zxc == _TypedDictMeta)) # True
# print(issubclass(type(zxc), _TypedDictMeta)) # True
# print(issubclass(zxc, _TypedDictMeta)) # False
# print(issubclass(TypedDict, zxc)) # TypeError('TypedDict does not support instance and class checks')
# print(issubclass(Typeddict, dict)) # True

# print(is_dataclass(Dataclass))

# z = {1:2}


class Z(int):
    pass


z = Z
x = None

print(issubclass(z, Z))  # True
print(issubclass(z, int))  # True
print(issubclass(z, dict))  # False
print(issubclass(x, int))  # TypeError: issubclass() arg 1 must be a class


# a = dict

# b = [1,2,3]
# c = [1,2,3]

# d = a(zip(b,c))
# print(d)


# print(type({}))

a = 1
print(a)

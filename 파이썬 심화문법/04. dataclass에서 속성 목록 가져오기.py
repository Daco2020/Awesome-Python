# dict는 어떻게 가져오나?
dict = {"a":2,"b":4,"c":6}

print(dict["a"]) # 2
print(dict["b"]) # 4
print(dict["c"]) # 6

print(dict.keys()) # dict_keys(['a', 'b', 'c'])


# dataclass로 속성 목록을 가져오자.
from dataclasses import dataclass, fields

@dataclass(frozen=True)
class Dataclass:
    a:int
    b:int
    c:int

data = Dataclass(a=1,b=3,c=5)
print(data)

print(data.a) # 1
print(data.b) # 3
print(data.c) # 5

print(fields(data))
"""(
Field(name='a',type=<class 'int'>,default=<dataclasses._MISSING_TYPE object at 0x104a83850>,default_factory=<dataclasses._MISSING_TYPE object at 0x104a83850>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD),
Field(name='b',type=<class 'int'>,default=<dataclasses._MISSING_TYPE object at 0x104a83850>,default_factory=<dataclasses._MISSING_TYPE object at 0x104a83850>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 
Field(name='c',type=<class 'int'>,default=<dataclasses._MISSING_TYPE object at 0x104a83850>,default_factory=<dataclasses._MISSING_TYPE object at 0x104a83850>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)
)"""

print(type(fields(data)[0].init)) # <class 'bool'> # field도 객체이다!
print([field.name for field in fields(data)]) # ['a', 'b', 'c']


print(data.keys()) # 'Dataclass' object has no attribute 'keys'

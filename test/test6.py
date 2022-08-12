
from dataclasses import dataclass, fields, is_dataclass


@dataclass(frozen=True)
class Data:
    a: str


data = Data(a=[])
print(data)

dict = {"a": ["asd"], "b": 0}
print(dict["a"] != [])
print(dict["b"] is not None)

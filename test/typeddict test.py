from collections import defaultdict
from typing import TypedDict


class OHLCV(TypedDict):
    a: str
    b: str
    c: str
    d: str


data = [{
    "a": "d",
    "b": "d",
    "c": "d",
}, {
    "a": "d",
    "b": "d",
    "c": "d",
}]

d = "dd"

print("a")
print(
    [OHLCV(**each, dt=d)
     for each in data]
)
print("b")
print(
    [{**each, "dt": d}
     for each in data]
)

"""
a
[{'a': 'd', 'b': 'd', 'c': 'd', 'dt': 'dd'}, {
    'a': 'd', 'b': 'd', 'c': 'd', 'dt': 'dd'}]
b
[{'a': 'd', 'b': 'd', 'c': 'd', 'dt': 'dd'}, {
    'a': 'd', 'b': 'd', 'c': 'd', 'dt': 'dd'}]
"""


q = {1: None}
z = q[1]
print(z)


a = defaultdict(int)
print(a)

a["qwe"] = "1"
print(a)

c = [None, None, 0]
a = filter(None, c)
print(any(c))


e = [i for i in c if i is not None]
print(e)
print(sum(e))

print(e == [])


dict = {"v": None}
print(dict.get("v", 0))

z = {"asd": None}
print(z["zxc"])

# c = sum(None, 1)
# print(c)

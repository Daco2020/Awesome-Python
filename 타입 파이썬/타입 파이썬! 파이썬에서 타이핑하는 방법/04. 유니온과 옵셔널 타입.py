# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

from typing import Union

xxx: Union[int, str] = 3

xxx = "17"


def foo(x: Union[int, str]) -> Union[int, str]:
    return x


foo(xxx)


# * Optional type

from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


xxx: Optional[str] = foo("amamov")

# Optional[str] == Union[str, None]
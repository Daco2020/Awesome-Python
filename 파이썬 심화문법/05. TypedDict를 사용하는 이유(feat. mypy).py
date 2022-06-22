from typing import TypedDict, Any, Dict

# 변수 준비
any_dict = {"a": "문자", "b": 1, "c": [1, 2, 3]}


# 함수 준비
def any_foo(dict: dict) -> Dict[str, Any]:
    return dict


# test1 - any_dict1 정상결과 여부 :: True
any_dict1 = any_foo(any_dict)
print("any_dict1 정상결과 여부 ::",
      isinstance(any_dict1["a"], str) and
      isinstance(any_dict1["b"], int) and
      isinstance(any_dict1["c"], list)
      )

# test2 - any_dict2 정상결과 여부 :: False
any_dict["a"] = 100
any_dict2 = any_foo(any_dict)
print("any_dict2 정상결과 여부 ::",
      isinstance(any_dict2["a"], str) and
      isinstance(any_dict2["b"], int) and
      isinstance(any_dict2["c"], list)
      )


# -------------

# TypedDict 준비
class DictType(TypedDict):
    a: str
    b: int
    c: list


# 변수 준비
typed_dict = DictType(a="문자", b=1, c=[1, 2, 3])

# 타입은 dict
print(type(typed_dict))  # <class 'dict'>
# 타입은 딕트이나 내부 속성의 타입들을 체크해줌

# 만약 클래스로 감싸지 않으면 같은 dict 임에도 서로 다른 타입으로 체크함
# typed_dict = {"a": "문자", "b": 1, "c": [1, 2, 3]}
# # Argument 1 to "typed_foo" has incompatible type "Dict[str, object]"; expected "DictType"


# 함수 준비
def typed_foo(dict: DictType) -> DictType:
    return dict


# test1 - typed_dict1 정상결과 여부 :: True
typed_dict1 = typed_foo(typed_dict)
print("typed_dict1 정상결과 여부 ::",
      isinstance(typed_dict1["a"], str) and
      isinstance(typed_dict1["b"], int) and
      isinstance(typed_dict1["c"], list)
      )


# test2 - typed_dict2 정상결과 여부 :: False
# # error: Argument 2 has incompatible type "int"; expected "str"
typed_dict["a"] = 100
typed_dict2 = typed_foo(typed_dict)
print("typed_dict2 정상결과 여부 ::",
      isinstance(typed_dict2["a"], str) and
      isinstance(typed_dict2["b"], int) and
      isinstance(typed_dict2["c"], list)
      )

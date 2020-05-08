"""
@File: stu.py
@CreateTime: 2020/4/27 下午4:46
@Desc: python数据类型使用
"""
from typing import List, Tuple, Dict, Mapping, NoReturn, Any
from typing import TypeVar


def test():
    var: List[int or float] = [2, 3.5, 6]
    var: List[List[int or str]] = [[1, 2], ["a", "b"]]


def size_abc(receive: Mapping[str, int]) -> Dict[str, str or int]:
    return {"code": 0, "message": "success"}


def hello() -> NoReturn:
    print("hello")


def add(num: Any) -> Any:
    return num + 1


# 自定义兼容类型
MyData = TypeVar('MyData', int, float, str)


def get_height() -> MyData:
    return 20























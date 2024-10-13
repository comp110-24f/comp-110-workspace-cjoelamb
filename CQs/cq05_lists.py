"""Mutating functions"""

__author__ = "730521229"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)

def double(a: list[int]) -> None:
    index: int = 0
    while index < len(a):
        a[index] *= 2
        index += 1

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(a = list_2)
print(list_1)
print(list_2)
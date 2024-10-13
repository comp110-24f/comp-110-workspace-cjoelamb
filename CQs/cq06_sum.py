"""Summing the elements of a list using different loops"""

__author__ = "730521229"


def w_sum(vals: list[float]) -> float:
    sum = 0.0
    index = 0

    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum

def f_sum(vals: list[float]) -> float:
    sum = 0.0

    for value in vals:
        sum += value
    return sum

def f_range_sum(vals: list[float]) -> float:
    sum = 0.0

    for index in range(len(vals)):
        sum += vals[index]
    return sum


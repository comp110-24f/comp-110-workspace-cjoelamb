"""cq04: Coordinates"""

__author__ = "730521229"


def get_coords(xs: str, ys: str) -> None:
    index_xs: int = 0  # sets initial index for xs
    while index_xs < len(xs):  # iterates over each chracter in xs
        index_ys: int = 0  # sets initial index for ys
        while index_ys < len(ys):  # iterates over each chracter in ys
            print(
                str((xs[index_xs], ys[index_ys]))
            )  # prints the matching index from each paramter
            index_ys += 1
        index_xs += 1

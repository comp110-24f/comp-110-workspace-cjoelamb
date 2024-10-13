"""My First CQ in COMP110!"""

__author__ = "730521229"


def mimic(message: str) -> str:
    """Defining mimic function which takes the input and repeats it back"""
    return message


def main() -> None:
    """Prints result of calling mimic"""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()

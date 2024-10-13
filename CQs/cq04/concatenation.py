"""cq04: Concatenation"""

__author__ = "730521229"


def concat(input1: str, input2: str) -> str:
    # combines two strings
    return input1 + input2


# creating global variables
word1: str = "happy"
word2: str = "tuesday"

# makes it so function call does not occur when imported
if __name__ == "__main__":
    # calls concat using 2 global variables
    print(concat(word1, word2))

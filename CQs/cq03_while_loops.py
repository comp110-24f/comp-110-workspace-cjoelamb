"""While Loops Challenge Question"""

__author__ = "730521229"


def num_instances(
    phrase: str, search_char: str
) -> int:  # sets parameters of function as str and return of int
    count: int = 0  # sets initial count = 0 before loop
    index: int = 0  # makes the loop start at first character of phrase
    while index < len(phrase):  # sets end of loop to final character
        if (
            phrase[index] == search_char
        ):  # looks to see if current character is the search_char
            count = count + 1  # if previous line true, adds to the count
        index = index + 1  # makes loop look at next character in phrase
    return count  # returns final number of the search characters in the phrase

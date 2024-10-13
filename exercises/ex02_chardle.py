"""Exercise #2: Chardle"""

__author__ = "730521229"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    # prompts user to enter 5 letter word
    word: str = input("Enter a 5-character word: ")

    # condition that checks length of entered word
    if len(word) != 5:
        # if entered word isn't 5 letters long, do this
        print("Error: Word must contain 5 characters.")
        exit()
    # regardless, do this
    return word


def input_letter() -> str:
    # prompts user to enter 1 letter character
    letter: str = input("Enter a single character: ")

    # condition that checks length of entered character
    if len(letter) != 1:
        # if entered character isn't 5 letters long, do this
        print("Error: Character must be a single character.")
        exit()
    # regradless, do this
    return letter


def contains_char(word: str, letter: str) -> None:
    # prints string involoving previous inputs
    print("Searching for " + str(letter) + " in " + str(word))

    # sets intital index at first character
    index = 0
    # sets initial count to 0
    count = 0
    # loop sets limit to search characters to length of word
    while index < len(word):
        # if current word character is the letter, do this
        if word[index] == letter:
            print(str(letter) + " found at index " + str(index))
            count += 1
        # goes to top of loop with new index
        index += 1
    # if loop never entered, do this
    if count == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    # if character only found once, do this
    elif count == 1:
        print("1 instance of " + str(letter) + " found in " + str(word))
    # if character found more than once, do this
    else:
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


if __name__ == "__main__":
    main()

"""Exercise 3: Wordle"""

__author__ = "730521229"


def input_guess(secret_word_len: int) -> str:
    """Asks for user input of guess of given length"""
    #guess takes value of the inputed word 
    guess: str = input(f"Enter a {secret_word_len} character word: ")
   
    #enter loop if length of guess is not equal to previously specified length
    while len(guess) != secret_word_len:
        #if while condition is true, input a new guess
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    #when while condition is false, return the guess
    return guess

def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searches to see if the inputed character is present in the secret word"""
    #ensures single letter char_guess
    assert len(char_guess) == 1
    #sets initial index
    secret_word_index: int = 0

    #loop through word
    while secret_word_index < len(secret_word):
        #checks if current character is the same
        if char_guess == secret_word[secret_word_index]:
            #if characters match, Return True and exit
            return True
        #if false, search for next character
        secret_word_index += 1
    #after searching through whole word, if character not found return  False
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks to see how well your word guess matches with the secret word, and returns different
colored boxes based on if the current character its looking at from word guess is in the secret 
word at all, and if it is in the same position as the secret word"""
   
    #length of guess must be the same as secret word
    assert len(guess) == len(secret)
   
    #gives local variables value of a colored box
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
   
    #gives initial output where boxes can be added to on the same line
    emoji_string: str = ""
    #sets initial index
    index: int = 0
    
    #loops through word
    while index < len(secret):
        #if current character from guess is in the same index as secret word
        if guess[index] == secret[index]:
            #adds green box to the string
            emoji_string += GREEN_BOX
        #after first is false, checks if current character is in secret word at all
        elif contains_char(secret, guess[index]):
            #adds yellow box
            emoji_string += YELLOW_BOX
        #neither above true, adds white box
        else:
            emoji_string += WHITE_BOX
        #start loop at new index
        index += 1

    return emoji_string

def main(secret: str) -> None:
    """The Entrypoint of the program and main game loop."""
    #Variables that track the state of the game
    maximum_turns: int = 6
    turn: int = 0
    won: bool = False
    
    #makes sure game is still in play
    while turn < maximum_turns and not won:
        turn += 1
        print(f"=== Turn {turn}/{maximum_turns} ===")

        #get a valid input for a guess
        guess = input_guess(secret_word_len = len(secret))

        #get emoji string for guess
        emoji_string = emojified(guess, secret)
        print(emoji_string)

        if guess == secret:
            won = True

    if won:
        print(f"You won in {turn}/{maximum_turns} turns!")
    else:
        print(f"X/{maximum_turns} - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret="codes")


    
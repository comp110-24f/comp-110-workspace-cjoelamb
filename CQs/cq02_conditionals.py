"""Challenge Question 02, Guess a Number"""

__author__ = "730521229"


def guess_a_number() -> (
    None
):  # defines function with no inputs and doesn't return anything
    secret = 7  # creates local variable secret which is equal to integer 7
    x = int(input("Guess a number: "))  # prompts terminal to ask for input (my guess)
    print(
        "Your guess was " + str(x)
    )  # prints my guess (turning guess into str so it can print)
    if x == secret:
        print("You got it!")  # if guess is right
    elif x < secret:
        print(
            "Your guess was too low! The secret number is " + str(secret)
        )  # if first is false, do this
    else:
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # if both false, do this


if __name__ == "__main__":
    guess_a_number()

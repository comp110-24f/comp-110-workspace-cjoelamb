"""Tea Party Planning"""

__author__ = "730521229"


def main_planner(guests: int) -> None:
    """
    Defining main_planner function, listing what all will be needed and its cost.
    Putting "guests" in each function call passes that parameter to each function,
    kind of replacing people with guests as the parameter. Adding str() to make sure
    it is printing a string rather than int or float
    """
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("cost: " + "$" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Defining the tea_bags function, giving 2 tea bags for each attendee"""
    return people * 2


def treats(people: int) -> int:
    """Defining the treats function, giving 1.5 treats for each tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Defining cost function, calculates cost for each tea bag and treat needed
    when each tea bag cost 50 cents and each treat costs 75 cents
    """
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

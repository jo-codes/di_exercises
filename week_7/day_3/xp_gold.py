import random
from random import randrange
#  this is the second time i've had to import something, and then import from the imported library. is this just how this works in python? is there a way to do this in one line?

# Exercise 1 – Temperature Advice

#     Create a function called get_random_temp().
#         This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#         Test your function to make sure it generates expected results.

#     Change the get_random_temp() function:
#         Add a parameter to the function, named ‘season’.
#         Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#         Now that we’ve changed get_random_temp(), let’s change the main() function:
#             Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’. Make sure to display a meaningful prompt.
#             Use the season as an argument when calling get_random_temp().


def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 0)
    elif season == "spring":
        return random.randint(0, 16)
    elif season == "summer":
        return random.randint(16, 23)
    elif season == "fall":
        return random.randint(23, 40)


#     Create a function called main().
#         Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#         Inform the user of the temperature, together with a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#     Add more functionality to the main() function, writing some friendly advice relating to the temperature, if it is:
#         below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#         between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#         between 16 and 23
#         between 24 and 32
#         between 32 and 40

############################# Commented out main because of duplicate function below ###############################

# def main(season):
#     temp = get_random_temp(season)
#     print(f"The temperature now is {temp}.")

#     if temp < 0:
#         print("It's cold")
#     elif temp >= 0 and temp < 16:
#         print("Kind chilly")
#     elif temp >= 16 and temp < 23:
#         print("Mild weather")
#     elif temp >= 23 and temp < 32:
#         print("Pretty warm")
#     elif temp >= 32:
#         print("Really hot")


#########################

# season = input("What season are we in? ")
# main(season)

#########################

# Exercise 2 – Double Dice

#     Create a function that will simulate the rolling of a die. Call it throw_dice. It should return an integer between 1 and 6.

def throw_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice = [die1, die2]
    return dice


# throw_dice()

def throw_until_doubles():
    #
    doubles = False
    rolls = 0
    dice = []
    while not doubles:
        dice = throw_dice()
        rolls += 1
        if dice[0] == dice[1]:
            doubles = True
    return rolls


throw_until_doubles()

#     Create a function called throw_until_doubles.
#         It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
#         For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
#         This function should return the number of times it threw the dice in total. In the example above, it should return 3.


def main():
    list_of_doubles = []
    while len(list_of_doubles) < 100:
        list_of_doubles.append(throw_until_doubles())
    total_rolls = sum(list_of_doubles)
    average_rolls = total_rolls / len(list_of_doubles)
    print(f"It took {total_rolls} total rolls to reach 100 doubles")
    print(f"The average number of rolls to a double was {average_rolls}")


main()

#     Create a main function. It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you to decide on what data structure to use).
#     After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
#     Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.

#     For example:

#         If the results of the throws were as follows (your code would do 100 doubles, not just 3):
#             (1, 2), (3, 1), (5, 5)
#             (3, 3)
#             (2, 4), (1, 2), (3, 4), (2, 2)

#         Then my output would show something like this:
#             Total throws: 8
#             Average throws to reach doubles: 2.67.

# Daily challenge :

#     Get a string from the user. The user must provide a string that is 10 characters long.
#     Inform the user what the first and last characters of the string are
#     ‘Build’ the string up: print the first character, then the first 2, then the first 3, etc., until you print
#     the entire string.
#     Swap some of the characters around, then print out this jumbled-up string to the user. Be sure to label it appropriately.

from random import shuffle

my_string = input("Gimme a word (10 chars)! ")
str_len = len(my_string)
first_letter = my_string[0]
last_letter = my_string[str_len - 1]

print(
    f"The first letter is: {first_letter} and the last letter is: {last_letter}")

# loop increment one until length times
# print from range until increment

n = 0
while n < len(my_string) + 1:
    print(my_string[0: n])
    n += 1

my_string = list(my_string)
shuffle(my_string)

print(f"Your string in nonsensical fashion: {''.join(my_string)}")

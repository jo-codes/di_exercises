# Exercise

# Consider this list

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

#     Remove the Banana from the list
#     Remove “Blueberries” from the list.
#     Put “Kiwi” at the end of the list.
#     Add “Apples” at the beginning of the list
#     Count how many apples in the basket
#     empty the basket
#     print(basket)

#########################

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

################################

# Exercise 1

#     Create a set called my_fav_numbers with your favorites numbers.
#     Add two new numbers to it.
#     Remove the last one.
#     Create a set called friend_fav_numbers with your friend’s favorites numbers.
#     Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

############################

# my_fav_numbers = ([1, 2, 3, 4])
# my_fav_numbers.pop()
# friend_fav_numbers = ([5, 6, 7, 8])
# our_fav_numbers = my_fav_numbers + friend_fav_numbers

# print(our_fav_numbers)

##########################

# Exercise 2

#     Do the same exercise as Exercise 1 but with tuple

########################

# my_fav_numbers = (1, 2, 3, 4)
# n = len(my_fav_numbers)
# my_fav_numbers = my_fav_numbers[: n-1]
# friend_fav_numbers = (5, 6, 7, 8)
# our_fav_numbers = my_fav_numbers + friend_fav_numbers

# print(our_fav_numbers)

########################


# Exercise 3

#     Recap – What is a float? What is the difference between an integer and a float?
#     Earlier, we tried to create a sequence of floats. Did it work?
#     Can you think of another way of generating a sequence of floats?
#     Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

##############################

# list_of_floats = []
# num_to_add = 1.5

# while num_to_add <= 5:
#     list_of_floats.append(num_to_add)
#     num_to_add += .5

# print(list_of_floats)

##############################


# Exercise 4

#     Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value . As they enter each topping, print a message saying you’ll add that topping to their pizza .

#####################

# topping_or_quit = "wombat"

# while topping_or_quit != "quit":
#     topping_or_quit = input("Gimme a pizza topping ")
#     print(f"adding {topping_or_quit} to pizza")

# print("bye")

#####################


# Exercise 5
# Exercise 6

#     Given a list, use a while loop to print out every elements from the end to the beginning.

###############################

# my_list = ["this", "that", "the other"]
# counter = 0

# while counter < len(my_list):
#     print(my_list[counter])
#     counter += 1

# print("done")

###############################

# Exercise 7

# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .

# Take the last exercise, and apply it to a family, ask every member of the family their age, and at the end of the loop, tell them the cost of the tickets for the whole family.

#############################

# total = 0
# age = ""

# while True:
#     age = input("input age or q ")
#     if age == "q":
#         break
#     elif int(age) > 3 and int(age) < 12:
#         total += 10
#     elif int(age) > 12:
#         total += 15

# print(total)

#############################

# Exercise 8

# Given a list, use a while loop to print out every element which his index is even.

###########################

# my_list = ["a", "b", "c", "d", "e", "f"]
# index = 0
# while index < len(my_list):
#     if index % 2 == 0:
#         index += 1
#         continue
#     else:
#         print(my_list[index])
#         index += 1

###########################

# Exercise 9

# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which can see the movie.

#     Try to add the allowed ones to a list.

############################

# name = ""
# age = ""
# allowed_people = []

# while True:
#     age = input("input age or q ")
#     if age == "q" or name == "q":
#         break

#     name = input("input name or q ")
#     if age == "q" or name == "q":
#         break

#     if int(age) > 16 and int(age) < 21:
#         allowed_people.append(name)
#         print("enjoy the movie")
#     else:
#         print("go home, no movie for you")

# print(allowed_people)

############################


# Exercise 10

# This time you have a list of users, and you want to remove every user that is below 16 years old.
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.

# people = ["tommy", "tina", "timmy", "tony", "tanya"]
# index = len(people)
# while index > 0:
#     age = int(input("How old are you? "))
#     if age < 16:
#         del people[index: -1]
#     index -= 1

# print(people)

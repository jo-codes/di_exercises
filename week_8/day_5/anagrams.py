# Anagram checker

import anagram_checker
from anagram_checker import AnagramChecker

#     It should do the following:
#         Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
#         If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then validated:
#             Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
#             Only alphabetic characters are allowed. No numbers or special characters.
#             Whitespace should be removed from the start and end of the user’s input.
#         Once your code has decided that the user’s input is validated, it should find out:
#             if the user’s word is a valid English word, and all possible anagram words for the user’s word.
#             The above steps should be done by an instance of the AnagramChecker class.
#             Display the information about the word to the user in a user-friendly, nicely-formatted message on the screen. Something like this:
#             YOUR WORD :”MEAT”
#             this is a valid English word.
#             Anagrams for your word: mate,tame, team.
anagram = AnagramChecker()

word = ""
while word != "quit":
    anagrams = []
    word = input("Please enter a word to anagramize. Type 'quit' to quit. \n")
    if " " in word:
        print("\nSingle words only please \n")
        continue
    if anagram.is_valid(word):
        anagrams = anagram.is_anagram(word)
        print(f"\nYour anagrams are {anagrams} \n")
        anagrams = []
        continue
    else:
        print(f"\n{word} is not a word...\n")
        continue

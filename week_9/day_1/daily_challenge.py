# Daily Challenge

# Create a class that checks if a word is a palindrome (i.e. words that look the same written backwards).
# For example, if the word is “radar”, it should return True.

class Whydidyouaskmetomakeaclasswhenthisshouldjustbeafunction:
    def __init__(self):
        pass

    def actualfunction(self, word):
        if word == "".join(reversed(word)):
            print("Anagram")
        else:
            print("Not anagram")


word = input("Please pick a word to check for an anagram ")

anagram_checker = Whydidyouaskmetomakeaclasswhenthisshouldjustbeafunction()

anagram_checker.actualfunction(word)

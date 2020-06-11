# Anagram checker

# create a class called AnagramChecker
#     The class should have the following methods:
#         __init__ - should load the word list file (text file) into a variable, so that it can be searched later on.
#         is_valid_word(word) – should check if the given word (‘word’) is a valid word.
#         get_anagrams(word) – should find all anagrams for the given word. (eg. if ‘word’ is ‘meat’,the function should return a list containing [‘mate’, ‘tame’, ‘team’].)
#         (Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain exactly the same letters (but not in the exact same order), and False if not.)
#         Note: None of the methods of this class should print anything to output.

class AnagramChecker():
    words = []

    def __init__(self):

        with open("./sowpods.txt") as file:
            self.words = file.readlines()
            self.words = [x.strip() for x in self.words]

    def is_valid(self, word):
        word = word.upper()
        if word in self.words:
            return True
        else:
            return False

    def is_anagram(self, word):
        anagrams = []
        word = word.upper()
        sorted_word = sorted(word)

        for w in self.words:
            if word != w:
                if sorted(w) == sorted_word:
                    anagrams.append(w)
        return anagrams

import itertools
# batteries included!

# Daily challenge :

# Write a Python class to get all possible unique subsets from a set of distinct integers.
# Example:

# Input : [4, 5, 6]
# Expected Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Example :

# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Expected Output : [[-10, 2, 8], [-7, -3, 10]]

# Why does this have to be a class when all it has is one method?


class findsUniques:
    def __init__(self):
        pass

    def find_uniques(self, arr):
        for item in range(0, len(arr)+1):
            for subset in itertools.combinations(arr, item):
                print(subset)


unique_finder = findsUniques()
unique_finder.find_uniques([5, 6, 7])


class sumsToZero:
    def __init__(self):
        pass

    def find_sums(self, arr):
        n = len(arr)
        found = True
        for i in range(0, n-2):

            for j in range(i+1, n-1):

                for k in range(j+1, n):

                    if (arr[i] + arr[j] + arr[k] == 0):
                        print(arr[i], arr[j], arr[k])
                        found = True

        if (found == False):
            print(" not exist ")


find_three = sumsToZero()
find_three.find_sums([0, -1, 2, -3, 1])

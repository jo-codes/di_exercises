# Hint: Look at the remote learning “Matrix”
# Daily challenge : Solve the Matrix

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alphanumeric characters and connect them, then he replaces every group of symbols between two alphanumeric characters by a space.

# Using his technique, try to decode this matrix:

matrix = [
    ["7 3"],
    ["Tsi"],
    ["h%x"],
    ["i #"],
    ["sM "],
    ["$a "],
    ["#t%"],
    ["ir!"]
]

index = matrix[0]
width = len(index[0])
length = len(matrix)
message = ""

i = 0
while i < width:
    for line in matrix:
        message += line[0][i]
    i += 1

for char in message:
    if not char.isalnum():
        message = message.replace(char, " ")

print(message)

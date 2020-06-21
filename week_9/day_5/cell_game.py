# Create a Cell Game.
# A cell game is a game that simulate evolution, it's a 0 player game, it means that the game starts with an initial state, and run alone.
# The initial state is a grid (of any size) with some cells that can be dead or alive. For example:
# _ _ _ _ *
# _ * * _ *
# _ * _ _ _
# * * _ * _
# * _ * * _
# This is a 5x5 grid, every _ is a dead cell, and every * is an alive one. When the game starts, it simulates generation, at each generation, the grid changes following these rules:
# Any live cell with fewer than two live neighbors dies, as if caused by under population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Create a program that simulate one generation, and then another that simulate n (a number given by the user) generations and print the output grid.


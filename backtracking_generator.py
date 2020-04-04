import numpy as np
import helper
import random

### SQUARE CHECK PENDING ###

def generate(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                for m in range(1,len(grid)+1):
                    if helper.backtrack_check(i,j,m,grid):
                        grid[i][j] = m
                        generate(grid)
                        if np.count_nonzero(np.array(grid))==len(grid)*len(grid):
                            return grid
                        grid[i][j] = 0
                return  # No solution, Backtrack  

def initialize():
    grid = []
    for i in range(9):
        t = []
        for j in range(9):
            t.append(0)
        grid.append(t)

    grid[0]=random.sample([1,2,3,4,5,6,7,8,9], len([1,2,3,4,5,6,7,8,9]))

    col = []
    for i in range(1,10):
        if i!=grid[0][0]:
            col.append(i)

    colshuffled = random.sample(col, len(col))

    for i in range(1,9):
        grid[i][0] = colshuffled[i-1]

    return grid

grid = initialize()
helper.display(grid)
generate(grid)
helper.display(grid)
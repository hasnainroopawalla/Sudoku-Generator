import numpy as np

def check(i,j,m,grid):
    rowflag = 0
    colflag = 0

    #row
    for jj in range(len(grid)):
        if grid[i][jj] == m:
            rowflag = 1
            break

    #col
    for ii in range(len(grid)): 
        if grid[ii][j] == m:
            colflag = 1
            break

    if rowflag==1 or colflag==1:
        return False
    else:
        return True

def generate(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                for m in range(1,len(grid)+1):
                    if check(i,j,m,grid):
                        grid[i][j] = m
                        generate(grid)
                        if np.count_nonzero(np.array(grid))==len(grid)*len(grid):
                            return grid
                        grid[i][j] = 0
                return  # No solution, Backtrack
                   

def solve(grid): 
	return generate(grid)
def saveboard(board):
    with open('generated-boards.txt', 'a') as f:
        for item in board:
            f.write("%s\n" % item)
        f.write('\n\n')

def display(a):
    print()
    for i in range(len(a)):
        if i%3==0 and i!=0:
            print('------+-------+-------')
        for j in range(len(a[i])):
            if j%3==0 and j!=0:
                print('|', end =" ")
            if a[i][j]!=0:
                print(a[i][j], end =" ")
            else:
                print(' ', end =" ")
        print()
    print()


def backtrack_check(i,j,m,grid):
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
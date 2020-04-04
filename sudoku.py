import random
import time
import solver

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


def checkboard(a, l):

    # ROWS
    rowflag = 0
    for i in a:
        if len(l.difference(set(i)))!=0:
            rowflag = 1
            break

    # COLUMNS
    colflag = 0
    for i in range(9):
        cols = []
        for j in range(9):
            cols.append(a[j][i])    
        if len(l.difference(set(cols)))!=0:
            colflag = 1
            break
        
    if rowflag==1 or colflag==1:
        return False
    else:
        return True

def getsquares(a):
    s1 = []
    for j in range(3):
        for k in range(3):
            s1.append(a[j][k])
            
    s2 = []
    for j in range(3):
        for k in range(3,6):
            s2.append(a[j][k])
      
    s3 = []
    for j in range(3):
        for k in range(6,9):
            s3.append(a[j][k])
      

    s4 = []
    for j in range(3,6):
        for k in range(3):
            s4.append(a[j][k])
            
    s5 = []
    for j in range(3,6):
        for k in range(3,6):
            s5.append(a[j][k])
      
    
    s6 = []
    for j in range(3,6):
        for k in range(6,9):
            s6.append(a[j][k])
      
    s7 = []
    for j in range(6,9):
        for k in range(3):
            s7.append(a[j][k])
            
    s8 = []
    for j in range(6,9):
        for k in range(3,6):
            s8.append(a[j][k])
      
    s9 = []
    for j in range(6,9):
        for k in range(6,9):
            s9.append(a[j][k])

    return s1,s2,s3,s4,s5,s6,s7,s8,s9
    
def generateboard(l):
    
    b =  [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,4,9,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]


##    b = [[7, 5, 2, 9, 8, 4, 1, 3, 6],
##         [3, 1, 8, 6, 5, 2, 4, 9, 7],
##         [6, 4, 9, 1, 7, 3, 5, 2, 8],
##         [8, 2, 7, 5, 3, 9, 6, 1, 4],
##         [1, 6, 3, 7, 4, 8, 2, 5, 9],
##         [5, 9, 4, 2, 1, 6, 8, 7, 3],
##         [9, 7, 5, 8, 6, 1, 3, 4, 2],
##         [2, 3, 6, 4, 9, 5, 7, 8, 1],
##         [4, 8, 1, 3, 2, 7, 9, 6, 5]]

    c = 0
    while c!=9:
        n = 0
        temp = []
        flag = 0
        rancount = 0
        #print(c)
        while flag==0:  # To check if row is complete
            n+=1
            #print(c,n,temp)
            if(b[c][len(temp)]!=0):
                temp.append(b[c][len(temp)])
                continue
            num = random.randrange(1,10)
            rancount+=1
        
            
            if rancount==50:   # Threshold = 50; Generate row again     
                #print(temp)
                random.seed(time.time())
                temp = []       
                rancount = 0
                
            if not num in temp:
                cflag = 0
                for i in range(len(b)):
                    if b[i][len(temp)]==num:
                        cflag = 1                   
                        break

                if cflag==0:
                    
                    s1,s2,s3,s4,s5,s6,s7,s8,s9 = getsquares(b)

                    if (c==0 or c==1 or c==2) and (len(temp)==0 or len(temp)==1 or len(temp)==2):
                        if num not in s1:
                            temp.append(num)
                    elif (c==0 or c==1 or c==2) and (len(temp)==3 or len(temp)==4 or len(temp)==5):
                        if num not in s2:
                            temp.append(num)
                    elif (c==0 or c==1 or c==2) and (len(temp)==6 or len(temp)==7 or len(temp)==8):
                        if num not in s3:
                            temp.append(num)

                    if (c==3 or c==4 or c==5) and (len(temp)==0 or len(temp)==1 or len(temp)==2):
                        if num not in s4:
                            temp.append(num)
                    elif (c==3 or c==4 or c==5) and (len(temp)==3 or len(temp)==4 or len(temp)==5):
                        if num not in s5:
                            temp.append(num)
                    elif (c==3 or c==4 or c==5) and (len(temp)==6 or len(temp)==7 or len(temp)==8):
                        if num not in s6:
                            temp.append(num)

                    if (c==6 or c==7 or c==8) and (len(temp)==0 or len(temp)==1 or len(temp)==2):
                        if num not in s7:
                            temp.append(num)
                    elif (c==6 or c==7 or c==8) and (len(temp)==3 or len(temp)==4 or len(temp)==5):
                        if num not in s8:
                            temp.append(num)
                    elif (c==6 or c==7 or c==8) and (len(temp)==6 or len(temp)==7 or len(temp)==8):
                        if num not in s9:
                            temp.append(num)

            
            if(len(temp)==9):
                flag = 1
                
        b[c]=temp
        c+=1
    return b

def question(grid, difficulty):
    if difficulty==1:
        clear = [4,5,6] # clear 4,5,6 values per row
    elif difficulty==2:
        clear = [5,6]
    else:
        clear = [6,7]

    for i in range(len(grid)):
        numclear = random.choice(clear)
        clearflag = 0

        while clearflag!=numclear:
            element = random.choice(grid[i])
            if element != 0:
                grid[i][grid[i].index(element)] = 0
                clearflag+=1

    return grid

l = {1,2,3,4,5,6,7,8,9}

start = time.time()
board = generateboard(l)
display(board)
saveboard(board)
end = time.time()
print('Time to generate:',round(end-start,2),'seconds')


difficulty = int(input('1- Easy\n2- Medium\n3- Hard\n'))
print('Puzzle:')
qstn = question(board,difficulty)
display(qstn)

if input('Press s to solve: ')=='s':
    ans = solver.solve(qstn)
    display(ans)


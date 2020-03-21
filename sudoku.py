import random

def display(a):
    print()
    for i in range(len(a)):
        if i%3==0 and i!=0:
            print('------+-------+-------')
        for j in range(len(a[i])):
            if j%3==0 and j!=0:
                print('|', end =" ")
            print(a[i][j], end =" ")
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
        
    if rowflag==1 or colflag==1 or not checksquares(a):
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
    b = [[3,2,9,5,4,7,6,1,8]]
    
    b =  [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

##    b = [[3,2,9,5,4,7,6,1,8],
##        [6,5,8,9,1,3,4,2,7],
##         [4,1,7,2,8,6,9,5,3],
##         [9,7,3,1,5,2,8,4,6],
##         [5,6,2,8,7,4,3,9,1],
##         [8,4,1,6,3,9,2,7,5],
##         [1,9,4,3,6,5,7,8,2],
##         [7,3,5,4,2,8,1,6,9],
##         [2,8,6,7,9,1,5,3,4]]
    
    c = 0
    while c!=9:
        temp = []
        flag = 0
        rancount = 0
        
        while flag==0:
            num = random.randrange(1,10)
            rancount+=1
            print(c+1,rancount)
            print(temp)
            
            if rancount==50:
                temp=[]
                rancount = 0
                
            if not num in temp:
                cflag = 0
                for i in range(len(b)):
                    #print(b[i][len(temp)])
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
        #s1,s2,s3,s4,s5,s6,s7,s8,s9 = getsquares(b)
        
    return b

    

l = {1,2,3,4,5,6,7,8,9}

a = [[3,2,9,5,4,7,6,1,8],
     [6,5,8,9,1,3,4,2,7],
     [4,1,7,2,8,6,9,5,3],
     [9,7,3,1,5,2,8,4,6],
     [5,6,2,8,7,4,3,9,1],
     [8,4,1,6,3,9,2,7,5],
     [1,9,4,3,6,5,7,8,2],
     [7,3,5,4,2,8,1,6,9],
     [2,8,6,7,9,1,5,3,4]]


board = generateboard(l)
display(board)

with open('board.txt', 'a') as f:
    for item in board:
        f.write('\n\n')
        f.write("%s\n" % item)
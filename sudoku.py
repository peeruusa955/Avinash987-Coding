# Solving Sudoku by Backtracking
import numpy as np
mat = []
# mat = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]


#Check implicit conditions
def isPossible(y, x, n):
    #print("Checking Possibilities of "+ str(n) +" in position "+ str(y) +" "+ str(x) +"" )
    global mat
    # Check in the Row
    for i in range(0,9):
        if mat[y][i] == n:
            return False
    # Check in the Column
    for i in range (0,9):
        if mat[i][x] == n:
            return False
    # Check in the square
    y0, x0 =  (y//3) * 3, (x//3) * 3
    for j in range(y0, y0+3):
        for k in range(x0, x0+3):
            if mat[j][k] == n:
                return False
    return True

def Solve():
    # Backtracking
    global mat
    for y in range(9):
        for x in range(9):
            if(mat[y][x] == 0):
                # print("Find a number position "+ str(y) +" "+ str(x) +"" )
                for n in range(1, 10):
                    if(isPossible(y,x,n)):
                        # print("Found "+ str(n) +" in position "+ str(y) +" "+ str(x) +"" )
                        mat[y][x] = n
                        if Solve():
                            return True
                        mat[y][x] = 0
                return False
    for row in mat:
        print(*row, end=' ')
    exit()
    #input("More?")
if __name__ == "__main__":

    # print("Enter all the values of sudoku if empty fill them with 0")
    T = int(input())
    for t in range(T):
        list1 = [int(item) for item in input().split()]
        mat = [list1[i : i+9] for i in range(0, len(list1), 9)]
        Solve()
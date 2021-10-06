'''
PROGRAM DESCRIPTION:

create sudoko game using numpy module and oops concept
'''

#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:4-10-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None


#This game is played automatically by the program by solving sudoko using backtracking

import numpy as np

class suduko:

    #checking value n is  present in row column or block
    def isSafe(self,board,i,j,n):

        # checking value is  present in column if present return False(unsafe)
        for k in range(0,9):
            #print(k)
            if(board[i][k]==n):
                return False

        # checking value is  present in row if present return False(unsafe)
        for k in range(0,9):
            #print(k)
            if(board[k][j]==n):
                return False



        # checking value is  present in block if present return False(unsafe)

        # start row and start column position of block containing the current cell
        rs=i-(i%3)
        cs=j-(j%3)
        for i in range(0,3):
            for j in range(0,3):
                if(board[rs+i][cs+j]==n):
                    return False
        return True



    #solving sudoko using backtracking
    def solve(self,board, r, c):

        #current row
        row = r
        col = 0
        empty=False

        #checking for empty cell
        while row < 9:
            col = 0

            while col < 9:
                if (board[row][col] == 0):
                    empty=True # if we got empty cell stop search  break inner while
                    break
                col += 1

            #break outer while if got empty cell
            if(empty):
                break
            row += 1

        #if no empty cell sudoko is solved and return True
        if (row == 9 and col == 9):
            return True

        #if sudoko has not solved
        #then place value in the empty cell
        #try placing values from 1-9 in cell
        for n in range(1, 10):
            #checking value  n is  present in row column or block
            if (self.isSafe(board, row, col, n)):

                #if n is not present in row column or block of current cell place n at current cell
                board[row][col] = n

                print('value entered at ({} ,{}) is {}'.format(row,col,n))
                print()
                #printing updated board
                print('-----------------------board-------------------')

                print(board)

                #solving the remaining sudoko
                if (self.solve(board, row, col)):
                    return True
                else:
                    #if we cannot proceed further after trying 1-9 we undo previous move
                    board[row][col] = 0

                    print('undo value entered at ({} ,{}) '.format(row, col))
                    print()

                    #printing updated board after undoing the previous move
                    print('-----------------------board-------------------')
                    print(board)

        #after trying 1-9 i.e; In 1 to 9 values  nothing is safe we return false to undo previous move
        return False


#create board of sudoko
board=np.array(   [
            [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
            [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
            [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
            [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
            [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
            [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
            [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ]

])


obj=suduko()

#print initial sudoko
print('--------------initial board-------------')
print(board)
print()
#solve sudoko
print(obj.solve(board,0,0))
print('--------solved sudoko-------')
print(board)

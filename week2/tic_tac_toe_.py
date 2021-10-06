'''
PROGRAM DESCRIPTION:
create tic_tac_toe game using numpy module and oops concept

'''

#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:4-10-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None


#This game is played automatically by the program by choosing random position to place the marker for a player

import random

import numpy as np

class tic_tac_toe:

    #board is made attribute of object
    def __init__(self):
        self.board=None

    def play_game(self,turns):

        self.create_board() #create board
        cnt=9 # total number of moves
        while cnt>0:
            for player in turns: #['X','O'] ['O','X']
                p=self.possibilities() #possible places to place
                print('______________________________________________')
                print(self.board)
                print('______________________________________________')
                print('possible positions:\n',p) # get possiblities

                #get random position to place the mark
                position=random.choice(p)

                self.place(player,position)#place the marker for current player in the position

                cnt-=1 # one move completed

                #print updated board
                print('______________________________________________')
                print(self.board)
                print('______________________________________________')

                #evaluate for the win
                win=self.evaluate_for_winner(player)
                if(win==-1): # board is empty means continue
                    continue
                #return winning player marker
                else:
                    return win



    #create board
    def create_board(self):
        board=np.full((3,3),'-',dtype='str')
        self.board=board


    #possibilities
    def possibilities(self):
        ans=np.where(self.board=='-')
        return list(zip(ans[0],ans[1]))



    #place marker for player
    def place(self,player,position):
        if(self.board[position]=='-'):
            self.board[position]=player



    #evaluation for win of player

    # row wise there is any match
    def row_win(self,player):
        for row in self.board:
            if (all([cell == player for cell in row])):
                return True
        else:
            return False

    #column wise there is any match

    def column_win(self, player):

        board = np.transpose(self.board)
        for col in board:
            if (all([cell == player for cell in col])):
                return True
        else:
            return False

    #diagonal wise there is any match
    def diagonal_win(self,player):
        if(np.all(np.diag(self.board)==player) or np.all(np.diag(np.fliplr(self.board))==player)):
            return True
        else:
            return False

    def evaluate_for_winner(self,player):
        #check row wise ,column wise or diagonal wise there is any match
        if(self.row_win(player) or
        self.column_win(player) or
        self.diagonal_win(player)):
            winner=player
            return winner
        else:
            #if board is  empty
            if(np.any(self.board=='-')):
                return -1

            #if board is not empty and no player won means draw
            else:
                return 'draw'







#create object for tic_tac_toe

obj=tic_tac_toe()

# how the turn should be X,O or O,X decide through input

turn1=input('enter whose gone take first turn:\n')
turn2=input('enter whose gone take second turn:\n')


#calling the play game
win=obj.play_game([turn1,turn2])

if(win!='draw'):
    print('winning player',win)
else:
    print('DRAW')






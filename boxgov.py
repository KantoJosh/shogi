from piece import Piece 
from utils import BOARD_SIZE

#Checklist 
# possible moves works

class BoxGovernance(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)


    def possibleMoves(self,board):  
        moves = []
        x,y = self.position 
        # up right = row ++ , col ++ (+1/+1)
        i = 1
        while ((x+i) < BOARD_SIZE and (y+i) < BOARD_SIZE and board[(x+i,y+i)] == None):
            moves.append([x+i,y+i])
            i += 1

        # up left = row ++, col --  (+1/-1)
        i = -1
        while (x+abs(i) < BOARD_SIZE and (y+i) >= 0 and board[(x+abs(i),y+i)] == None):
            moves.append([x+abs(i),y+i])
            i -= 1

        # down right = row --, col ++
        i = -1
        while (x+i >= 0 and (y+abs(i)) < BOARD_SIZE and board[(x+i,y+abs(i))] == None):
            moves.append([x+i,y+abs(i)])
            i -= 1

        # down left = row -- , col --
        i = -1
        while (x + i >= 0 and y + i >= 0 and board[(x+i,y+i)] == None):
            moves.append([x+i,y+i])
            i -= 1
        print("BOXGOV",moves)
        return moves

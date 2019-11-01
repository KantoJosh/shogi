from piece import Piece 
from utils import BOARD_SIZE

#Checklist 
# possible moves works

class BoxGovernance(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)

    # def getTopDiagonalMoves(self,board,size,row,column,offset):
    #     top_diag_moves = []
    #     while (row + offset < size and column < size):
    #         if board[(row,column)] != None:
    #             if board[(row,column)].player != self.player:
    #                 top_diag_moves.append([row,column])
    #                 break
    #             else:
    #                 break 
    #         else:
    #             moves.append([row,column])
    #             offset += 1

    def possibleMoves(self,board):  
        moves = []
        x,y = self.position 
        # up right = row ++ , col ++ (+1/+1)
        i = 1
        while ((x+i) < BOARD_SIZE and (y+i) < BOARD_SIZE):
            if board[(x+i,y+i)] != None:
                if board[(x+i,y+i)].player != self.player:
                    moves.append([x+i,y+i])
                    break
                else:
                    break 
            else:
                moves.append([x+i,y+i])
                i += 1

        # up left = row ++, col --  (+1/-1)
        i = -1
        while (x+abs(i) < BOARD_SIZE and (y+i) >= 0):
            if board[(x+abs(i),y+i)] != None:
                if board[(x+abs(i),y+i)].player != self.player:
                    moves.append([x+abs(i),y+i])
                    break 
                else:
                    break 
            else:
                moves.append([x+abs(i),y+i])
                i -= 1

        # down right = row --, col ++
        i = -1
        while (x+i >= 0 and (y+abs(i)) < BOARD_SIZE):
            if board[(x+i,y+abs(i))] != None:
                if board[(x+i,y+abs(i))].player != self.player:
                    moves.append([x+i,y+abs(i)])
                    break 
                else:
                    break 
            else:
                moves.append([x+i,y+abs(i)])
                i -= 1

        # down left = row -- , col --
        i = -1
        while (x + i >= 0 and y + i >= 0):
            if board[(x+i,y+i)] != None:
                if board[(x+i,y+i)].player != self.player:
                    moves.append([x+i,y+i])
                    break
                else:
                    break 
            else:
                moves.append([x+i,y+i])
                i -= 1
        print(moves)
        return moves

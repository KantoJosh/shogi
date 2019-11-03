from piece import Piece 
from utils import BOARD_SIZE
from boxdrive import BoxDrive
#Checklist 
# possible moves works

class BoxGovernance(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)

    # def possibleMoves(self,board):  
    #     moves = []
    #     x,y = self.position 
    #     # up right = row ++ , col ++ (+1/+1)
    #     i = 1
    #     while ((x+i) < BOARD_SIZE and (y+i) < BOARD_SIZE):
    #         if board[(x+i,y+i)] != None:
    #             if board[(x+i,y+i)].player != self.player:
    #                 moves.append((x+i,y+i))
    #                 break
    #             else:
    #                 break 
    #         else:
    #             moves.append((x+i,y+i))
    #             i += 1

    #     # up left = row ++, col --  (+1/-1)
    #     i = -1
    #     while (x+abs(i) < BOARD_SIZE and (y+i) >= 0):
    #         if board[(x+abs(i),y+i)] != None:
    #             if board[(x+abs(i),y+i)].player != self.player:
    #                 moves.append((x+abs(i),y+i))
    #                 break 
    #             else:
    #                 break 
    #         else:
    #             moves.append((x+abs(i),y+i))
    #             i -= 1

    #     # down right = row --, col ++
    #     i = -1
    #     while (x+i >= 0 and (y+abs(i)) < BOARD_SIZE):
    #         if board[(x+i,y+abs(i))] != None:
    #             if board[(x+i,y+abs(i))].player != self.player:
    #                 moves.append((x+i,y+abs(i)))
    #                 break 
    #             else:
    #                 break 
    #         else:
    #             moves.append((x+i,y+abs(i)))
    #             i -= 1

    #     # down left = row -- , col --
    #     i = -1
    #     while (x + i >= 0 and y + i >= 0):
    #         if board[(x+i,y+i)] != None:
    #             if board[(x+i,y+i)].player != self.player:
    #                 moves.append((x+i,y+i))
    #                 break
    #             else:
    #                 break 
    #         else:
    #             moves.append((x+i,y+i))
    #             i -= 1
    #     return moves

    def possibleMoves(board,position):  
        if board[position].promoted:
            moves = BoxDrive.possibleMoves(board,position)
        else:
            moves = []
        x,y = position 
        # up right = row ++ , col ++ (+1/+1)
        i = 1
        while ((x+i) < BOARD_SIZE and (y+i) < BOARD_SIZE):
            if board[(x+i,y+i)] != None:
                if board[(x+i,y+i)].player != board[position].player:
                    moves.append((x+i,y+i))
                    break
                else:
                    break 
            else:
                moves.append((x+i,y+i))
                i += 1

        # up left = row ++, col --  (+1/-1)
        i = -1
        while (x+abs(i) < BOARD_SIZE and (y+i) >= 0):
            if board[(x+abs(i),y+i)] != None:
                if board[(x+abs(i),y+i)].player != board[position].player:
                    moves.append((x+abs(i),y+i))
                    break 
                else:
                    break 
            else:
                moves.append((x+abs(i),y+i))
                i -= 1

        # down right = row --, col ++
        i = -1
        while (x+i >= 0 and (y+abs(i)) < BOARD_SIZE):
            if board[(x+i,y+abs(i))] != None:
                if board[(x+i,y+abs(i))].player != board[position].player:
                    moves.append((x+i,y+abs(i)))
                    break 
                else:
                    break 
            else:
                moves.append((x+i,y+abs(i)))
                i -= 1

        # down left = row -- , col --
        i = -1
        while (x + i >= 0 and y + i >= 0):
            if board[(x+i,y+i)] != None:
                if board[(x+i,y+i)].player != board[position].player:
                    moves.append((x+i,y+i))
                    break
                else:
                    break 
            else:
                moves.append((x+i,y+i))
                i -= 1
        return moves
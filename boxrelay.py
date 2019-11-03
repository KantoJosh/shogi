from piece import Piece 
from utils import BOARD_SIZE
from boxshield import BoxShield

class BoxRelay(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)

    
    # def possibleMoves(self,board): 
    #     if self.promoted:
    #         pass # return moves of Box Shield
        
    #     x,y = self.position
    #     offset = 1 if self.player == 0 else -1
    #     moves = [
    #         # diag
    #         (x + 1, y + 1),
    #         (x + 1, y - 1),
    #         # front of it -- only this one needs offset since other points 
    #         # dont change their coordinate based on orientation/which player the piece
    #         # belongs to
    #         (x + offset, y),
    #         # diagonal behind
    #         (x - 1, y + 1),
    #         (x - 1, y - 1)
    #     ]

    #     x = list(filter(lambda m: BOARD_SIZE > m[0] >= 0 and  0 <= m[1] < BOARD_SIZE
    #     and (board[m] == None or board[m].player != self.player),moves))
    #     #print(x)
    #     return x

    @staticmethod
    def possibleMoves(board,position): 
        if type(board[position]) != BoxRelay:
            raise ValueError("Piece must not be of type BoxRelay")
        if board[position].promoted:
            return BoxShield.possibleMoves(board,position)
        x,y = position
        offset = 1 if board[position].player == 0 else -1
        moves = [
            # diag
            (x + 1, y + 1),
            (x + 1, y - 1),
            # front of it -- only this one needs offset since other points 
            # dont change their coordinate based on orientation/which player the piece
            # belongs to
            (x + offset, y),
            # diagonal behind
            (x - 1, y + 1),
            (x - 1, y - 1)
        ]

        return list(filter(lambda m: BOARD_SIZE > m[0] >= 0 and  0 <= m[1] < BOARD_SIZE
        and (board[m] == None or board[m].player != board[position].player),moves))
    

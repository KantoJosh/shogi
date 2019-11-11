from piece import Piece 
from utils import BOARD_SIZE,LOWER,UPPER
from boxshield import BoxShield

class BoxRelay(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)

    @staticmethod
    def possibleMoves(board,position): 
        if board[position].promoted:
            return BoxShield.possibleMoves(board,position)
        x,y = position
        offset = 1 if board[position].player == LOWER else -1
        moves = {
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
        }

        return {m for m in moves if BOARD_SIZE > m[0] >= 0 and  0 <= m[1] < BOARD_SIZE and \
        (board.isEmptyAt(m) or board[m].player != board[position].player)}
    

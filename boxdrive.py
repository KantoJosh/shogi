from piece import Piece 
from utils import BOARD_SIZE

class BoxDrive(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    def possibleMoves(board,position):
        x,y = position
        moves = {
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
        }

        # filter coord based on whether
        # 1) coords are in bounds of array
        # 2) coords are either moving to an empty spot or an opponent's spot
        return {m for m in moves if 0 <= m[0] < BOARD_SIZE and 0 <= m[1] < BOARD_SIZE and \
        (board.isEmptyAt(m) or board[m].player != board[position].player)} 
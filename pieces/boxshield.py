from piece import Piece 
from utils import LOWER,UPPER,BOARD_SIZE
# Checklist
# possible move works !
class BoxShield(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    @staticmethod
    def possibleMoves(board,position): 
        x,y = position
        offset = 1 if board[position].player == LOWER else -1
        moves = {
            (x, y - 1),
            (x, y + 1),
            (x + offset, y + 1),
            (x + offset, y - 1),
            (x + offset, y),
            (x - offset, y),
        }

        return {m for m in moves if BOARD_SIZE > m[0] >= 0 and 0 <= m[1] < BOARD_SIZE and \
        (board.isEmptyAt(m) or board[m].player != board[position].player)}
from piece import Piece 
from boxshield import BoxShield
from utils import LOWER,UPPER,BOARD_SIZE

class BoxPreview(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    def possibleMoves(board,position): 
        if board[position].promoted:
            return BoxShield.possibleMoves(board,position)

        x,y = position
        offset = 1 if board[position].player == LOWER else -1
        if (BOARD_SIZE > (x + offset) >= 0) and \
        (BOARD_SIZE > (y) >= 0) and \
        (board.isEmptyAt((x + offset,y)) or board[(x + offset,y)].player != board[position].player):
            return {(x + offset,y)}
        else:
            return set()
    
    

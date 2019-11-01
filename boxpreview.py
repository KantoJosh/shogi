from piece import Piece 
from utils import LOWER,UPPER,BOARD_SIZE
# Checklist
# possible moves work
class BoxPreview(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    def possibleMoves(self,board): 
        x,y = self.position
        offset = 1 if self.player == LOWER else -1
        if (BOARD_SIZE > (x + offset) >= 0) and \
        (BOARD_SIZE >= (y) >= 0) and \
        (board[(x + offset,y)] == None or board[(x + offset,y)].player != self.player):
            print([x+offset,y])
            return [[x + offset,y]]
        else:
            return []
    
    

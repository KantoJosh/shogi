from piece import Piece 
from utils import LOWER,UPPER,BOARD_SIZE
# Checklist
# possible move works !
class BoxShield(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    
    # def possibleMoves(self,board): 
    #     offset = 1 if self.player == LOWER else -1
    #     moves = [
    #         # left
    #         (self.position[0], self.position[1] - 1),
    #         # right
    #         (self.position[0], self.position[1] + 1),

    #         (self.position[0] + offset, self.position[1] + 1),
    #         (self.position[0] + offset, self.position[1] - 1),
    #         (self.position[0] + offset, self.position[1]),
    #         (self.position[0] - offset, self.position[1]),
    #     ]
        
    #     x = list(filter(lambda m: BOARD_SIZE > m[0] >= 0 and 0 <= m[1] < BOARD_SIZE and 
    #     (board[m] == None or board[m].player != self.player),moves))
    #     #print(x)
    #     return x
    
    @staticmethod
    def possibleMoves(board,position): 
        x,y = position
        offset = 1 if board[position].player == LOWER else -1
        moves = [
            # left
            (x, y - 1),
            # right
            (x, y + 1),

            (x + offset, y + 1),
            (x + offset, y - 1),
            (x + offset, y),
            (x - offset, y),
        ]
        
        return list(filter(lambda m: BOARD_SIZE > m[0] >= 0 and 0 <= m[1] < BOARD_SIZE and 
        (board[m] == None or board[m].player != board[position].player),moves))
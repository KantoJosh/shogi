from piece import Piece 
from utils import BOARD_SIZE
# Checklist
# possible moves works
class BoxRelay(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)

    def possibleMoves(self,board): 
        offset = 1 if self.player == 0 else -1
        moves = [
            # diag
            [self.position[0] + 1, self.position[1] + 1],
            [self.position[0] + 1, self.position[1] - 1],
            # front of it -- only this one needs offset since other points 
            # dont change their coordinate based on orientation/which player the piece
            # belongs to
            [self.position[0] + offset, self.position[1]],
            # diagonal behind
            [self.position[0] - 1, self.position[1] + 1],
            [self.position[0] - 1, self.position[1] - 1]
        ]

        x = list(filter(lambda m: BOARD_SIZE > m[0] >= 0 and  0 <= m[1] < BOARD_SIZE
        and (board[(m[0],m[1])] == None or board[(m[0],m[1])].player != self.player),moves))
        print(x)
        return x
    

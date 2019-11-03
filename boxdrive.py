from piece import Piece 
from utils import BOARD_SIZE

# Checklist:
# 1 - possible moves work!

class BoxDrive(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    # def possibleMoves(self,board):
    #     moves = [
    #         (self.position[0] + 1, self.position[1] + 1),
    #         (self.position[0] + 1, self.position[1] - 1),
    #         (self.position[0] - 1, self.position[1] + 1),
    #         (self.position[0] - 1, self.position[1] - 1),
    #         (self.position[0] + 1, self.position[1]),
    #         (self.position[0], self.position[1] + 1),
    #         (self.position[0] - 1, self.position[1]),
    #         (self.position[0], self.position[1] - 1),
    #     ]

    #     # filter coord based on whether
    #     # 1) coords are in bounds of array
    #     # 2) coords are either moving to an empty spot or an opponent's spot
    #     return list(filter(lambda m: 0 <= m[0] < BOARD_SIZE and 0 <= m[1] < BOARD_SIZE and 
    #         (board[m] == None or board[m].player != self.player),
    #         moves))

    def possibleMoves(board,position):
        x,y = position
        moves = [
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
        ]

        # filter coord based on whether
        # 1) coords are in bounds of array
        # 2) coords are either moving to an empty spot or an opponent's spot
        return list(filter(lambda m: 0 <= m[0] < BOARD_SIZE and 0 <= m[1] < BOARD_SIZE and 
            (board[m] == None or board[m].player != board[position].player),
            moves))
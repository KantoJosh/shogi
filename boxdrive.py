from piece import Piece 
from utils import BOARD_SIZE

# Checklist:
# 1 - possible moves work!

class BoxDrive(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    def possibleMoves(self,board):
        moves = [
            [self.position[0] + 1, self.position[1] + 1],
            [self.position[0] + 1, self.position[1] - 1],
            [self.position[0] - 1, self.position[1] + 1],
            [self.position[0] - 1, self.position[1] - 1],
            [self.position[0] + 1, self.position[1]],
            [self.position[0], self.position[1] + 1],
            [self.position[0] - 1, self.position[1]],
            [self.position[0], self.position[1] - 1],
        ]

        # filter coord based on whether
        # 1) coords are in bounds of array
        # 2) coords are either moving to an empty spot or an opponent's spot
        return list(filter(lambda m: 0 <= m[0] < BOARD_SIZE and 0 <= m[1] < BOARD_SIZE and 
            (board[(m[0],m[1])] == None or board[(m[0],m[1])].player != self.player),
            moves))
        # possibleMoves = []
        # for move in moves:
        #     if 0 <= move[0] < BOARD_SIZE and 0 <= move[1] < BOARD_SIZE:
        #         if board[(move[0],move[1])] == None or board[(move[0],move[1])].player != self.player: 
        #             possibleMoves.append([move[0],move[1]])
        # print(possibleMoves)
        # return possibleMoves

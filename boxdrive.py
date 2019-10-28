from piece import Piece 

class BoxDrive(Piece):
    def __init__(self,row,column):
        Piece.__init__(self,row,column)
    
    def possibleMoves(self,board): # O(1)
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

        return list(filter(lambda m: m[0] >= 0 and m[1] < 5 and board[m[0]][m[1]] == None,moves))
    

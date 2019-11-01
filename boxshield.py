from piece import Piece 

class BoxShield(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    
    def possibleMoves(self,board): 
        moves = [
            [self.position[0], self.position[1] - 1],
            [self.position[0], self.position[1] + 1],
            [self.position[0] + 1, self.position[1] + 1],
            [self.position[0] + 1, self.position[1] - 1],
            [self.position[0] + 1, self.position[1]],
            [self.position[0] - 1, self.position[1]],
        ]

        return list(filter(lambda m: m[0] >= 0 and m[1] < 5,moves))

    
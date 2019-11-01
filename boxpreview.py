from piece import Piece 

class BoxPreview(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    def possibleMoves(self,board): 
        offset = 1 if self.player == 0 else -1
        if (4 >= (self.position[0] + offset) >= 0) and (4 >= (self.position[1]) >= 0):
            return [[self.position[0] + offset,self.position[1]]]
        else:
            return []
    
    

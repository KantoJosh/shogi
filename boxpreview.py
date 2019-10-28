from piece import Piece 

class BoxShield(Piece):
    def __init__(self,row,column):
        Piece.__init__(self,row,column)
    
    def possibleMoves(self): 
        if (4 >= (self.position[0] - 1) >= 0) and (4 >= (self.position[1]) >= 0):
            return [[self.position[0] - 1,self.position[1]]]
        else:
            return []
    
    

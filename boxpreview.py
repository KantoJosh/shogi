from piece import Piece 

class BoxShield(Piece):
    def __init__(self,row,column):
        Piece.__init__(self,row,column)
    
    def possibleMoves(self,board): 
        if board[self.position[0] - 1][self.position[1]] == None:
            return [[self.position[0] - 1,self.position[1]]]
        else:
            return []
    
    

from piece import Piece 

class BoxNote(Piece):
    def __init__(self,row,column):
        Piece.__init__(self,row,column)
    
    def possibleMoves(self): # O(1)
        rowMoves = [[i,self.position[1]] for i in range(5)]
        columnMoves = [[self.position[0],i] for i in range(5)]

        return list(filter(lambda m: m[0] >= 0 and m[1] < 5,rowMoves + columnMoves))
    


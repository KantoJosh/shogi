from piece import Piece 

class BoxNote(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    #TODO 
    # FIX, right now allows jumping over

    # def possibleMoves(self,board): # O(1)
    #     rowMoves = []
    #     for i in range(5):
    #         print(i,self.position[1])
    #         if board[(i,self.position[1])] != None:
    #             break
    #         rowMoves.append([i,self.position[1]])
        
    #     columnMoves = []
    #     for i in range(5):
    #         if board[(self.position[0],i)] != None:
    #             break
    #         columnMoves.append([self.position[0],i])


    #     #rowMoves = [[i,self.position[1]] for i in range(5)]
    #     #columnMoves = [[self.position[0],i] for i in range(5)]

    #     rowMoves = []
    #     columnMoves = []

    #     return list(filter(lambda m: m[0] >= 0 and m[1] < 5,rowMoves + columnMoves))
    
    def possibleMoves(self,board): # O(1)
        rowMoves = []
        # go from position to left border
        for i in range(self.position[1]-1,-1,-1):
            if board[(self.position[0],i)] != None:
                break
            rowMoves.append([self.position[0],i])

        # go from position to right border until object is detected
        for i in range(self.position[1]+1,5):
            if board[(self.position[0],i)] != None:
                break 
            rowMoves.append([self.position[0],i])
        
        columnMoves = []

        # go from position to top border until object is detected
        for j in range(self.position[0]-1,-1,-1):
            if board[(j,self.position[1])] != None:
                break
            columnMoves.append([j,self.position[1]])
        
        for j in range(self.position[0]+1,5):
            if board[(j,self.position[1])] != None:
                break
            columnMoves.append([j,self.position[1]])

        return list(filter(lambda m: m[0] >= 0 and m[1] < 5,rowMoves + columnMoves))

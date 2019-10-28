from piece import Piece 

class BoxGovernance(Piece):
    def __init__(self,row,column):
        Piece.__init__(self,row,column)
    
    def possibleMoves(self,board): 
        rightDiagonal = []
        leftDiagonal = []
        i = 0
        j = 4
        while (i <= 4):
            right.append([i,j])
            i += 1
            j -= 1

        i = 0
        j = 0
        while (i <= 4):
            leftDiagonal.append([i,j])
            i += 1
            j += 1

        return list(filter(lambda m: m[0] >= 0 and m[1] < 5 and board[m[0]][m[1]] == None,leftDiagonal + rightDiagonal))
    
    

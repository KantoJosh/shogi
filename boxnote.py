from piece import Piece 
from utils import BOARD_SIZE

# Checklist
# possible move works

class BoxNote(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    # def possibleMoves(self,board): # O(1)
    #     moves = []
    #     x,y = self.position

    #     # right of box note (row + 0, col + 1)
    #     i = 1
    #     while (y+i) < BOARD_SIZE and board[(x,y+i)] == None:
    #         moves.append([x,y+i])
    #         i += 1

    #     # left of box note (row + 0, col - 1)
    #     i = -1
    #     while (y+i) >= 0 and board[(x,y+i)] == None:
    #         moves.append([x,y+i])
    #         i -= 1

    #     i = 1
    #     # up of box note (row + 1, col)
    #     while (x+i) < BOARD_SIZE and board[(x+i,y)] == None:
    #         moves.append([x+i,y])
    #         i += 1

        
    #     # down of box note (row - 1, col)
    #     i = -1
    #     while (x + i) >= 0 and board[(x+i,y)] == None:
    #         moves.append([x+i,y])
    #         i -= 1

    #     return moves

    def possibleMoves(self,board): # O(1)
        moves = []
        x,y = self.position

        # right of box note (row + 0, col + 1)
        i = 1
        while (y+i) < BOARD_SIZE:
            if board[(x,y+i)] != None:
                if board[(x,y+i)].player != self.player:
                    moves.append([x,y+i])
                    break
                else:
                    break 
            else:
                moves.append([x,y+i])
                i += 1

        # left of box note (row + 0, col - 1)
        i = -1
        while (y+i) >= 0:
            if board[(x,y+i)] != None:
                if board[(x,y+i)].player != self.player:
                    moves.append([x,y+i])
                    break
                else:
                    break
            else:
                moves.append([x,y+i])
                i -= 1


        i = 1
        # up of box note (row + 1, col)
        while (x+i) < BOARD_SIZE:
            if board[(x+i,y)] != None:
                if board[(x+i,y)].player != self.player:
                    moves.append([x+i,y])
                    break
                else:
                    break
            else:
                moves.append([x+i,y])
                i += 1

        
        # down of box note (row - 1, col)
        i = -1
        while (x + i) >= 0:
            if board[(x+i,y)] != None:
                if board[(x+i,y)].player != self.player:
                    moves.append([x+i,y])
                    break
                else:
                    break 
            else:
                moves.append([x+i,y])
                i -= 1
        #print(moves)
        return moves


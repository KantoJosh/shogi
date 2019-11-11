from piece import Piece 
from utils import BOARD_SIZE
from boxdrive import BoxDrive

class BoxNote(Piece):
    def __init__(self,row,column,player):
        Piece.__init__(self,row,column,player)
    
    def possibleMoves(board,position): # O(1)
        if board[position].promoted:
            moves = BoxDrive.possibleMoves(board,position)
        else:
            moves = set()
            
        x,y = position
        # right of box note (row + 0, col + 1)
        i = 1
        while (y+i) < BOARD_SIZE:
            if board[(x,y+i)] != None:
                if board[(x,y+i)].player != board[position].player:
                    moves.add((x,y+i))
                    break
                else:
                    break 
            else:
                moves.add((x,y+i))
                i += 1

        # left of box note (row + 0, col - 1)
        i = -1
        while (y+i) >= 0:
            if board[(x,y+i)] != None:
                if board[(x,y+i)].player != board[position].player:
                    moves.add((x,y+i))
                    break
                else:
                    break
            else:
                moves.add((x,y+i))
                i -= 1


        i = 1
        # up of box note (row + 1, col)
        while (x+i) < BOARD_SIZE:
            if board[(x+i,y)] != None:
                if board[(x+i,y)].player != board[position].player:
                    moves.add((x+i,y))
                    break
                else:
                    break
            else:
                moves.add((x+i,y))
                i += 1

        
        # down of box note (row - 1, col)
        i = -1
        while (x + i) >= 0:
            if board[(x+i,y)] != None:
                if board[(x+i,y)].player != board[position].player:
                    moves.add((x+i,y))
                    break
                else:
                    break 
            else:
                moves.add((x+i,y))
                i -= 1

        return moves

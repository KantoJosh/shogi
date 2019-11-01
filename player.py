from utils import translate_square_coord
from piece import Piece
class Player():
    _player_id = 0
    def __init__(self):
        self._captured = {
            "d": [],
            "g": [],
            "n" : [],
            "s" : [],
            "r" : [],
            "p" : []
        }
        self.id = Player._player_id
        self.moves = 0
        Player._player_id += 1

    def capture(self,piece):
        if piece == None:
            raise ValueError("Cannot capture empty square")
        self._captured[Piece.getChar(piece).lower()].append(piece)

    
    def free(self,key):
        if key not in self._captured.keys():
            raise ValueError("Invalid piece was attempted to be dropped")
        if len(self._captured[key]) == 0:
            raise ValueError("Can not remove nonexistent piece from captured set")
        return self._captured[key].pop() 

    
    @property
    def captured(self):
        """Returns set of Piece objects"""
        return self._captured
    
    def drop(self,pieceChar,board,destination):
        dest_x,dest_y = destination
        if board[(dest_x,dest_y)] != None:
            raise ValueError("Cannot drop piece on another piece")
        piece = self.free(pieceChar)
        # update position of piece
        piece.setposition(destination)
        board[(dest_x,dest_y)] = piece 


    def move(self,source,destination,board):
        s_x,s_y = source
        d_x,d_y = destination
        if board[(s_x,s_y)] == None:
            raise ValueError("Cannot move empty square")
        captured_piece = board[(d_x,d_y)]
        
        if board[(s_x,s_y)].player != self.id:
            raise ValueError("Cannot move piece that isn't yours")

        if [d_x,d_y] not in board[(s_x,s_y)].possibleMoves(board):
            raise ValueError("Invalid move")

        if board[(d_x,d_y)] != None and self.id == captured_piece.player:
            raise ValueError("Cannot move onto your own piece")

        board[(s_x,s_y)].setposition((d_x,d_y))
        board[(d_x,d_y)] = board[(s_x,s_y)]
        board[(s_x,s_y)] = None
        self.moves += 1
        if captured_piece != None:
            # swap side of captured piece
            captured_piece.switchPlayers()

            self.capture(captured_piece)

            # reduce number of pieces other user has
    
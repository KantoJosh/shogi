from utils import translate_square_coord,LOWER,UPPER
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
        piece.demote()
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
        if not board.isEmpty(destination): 
            raise ValueError("Cannot drop piece on another piece")
        in_promo_zone = True if (destination[0] == LOWER and self.id == UPPER) or (destination[0] == UPPER and self.id == LOWER) else False
        if pieceChar == "p" and in_promo_zone: 
            raise ValueError("Cannot drop BoxPreview in promotion zone")
        elif pieceChar == "p" and False: # eventually change False to is_in_checkmate (immediate as of moving to destination)
            pass

        piece = self.free(pieceChar)
        piece.update_position(destination)
        board[destination] = piece 


    def move(self,source,destination,board,promote):  
        """Concerns with player's move: what they neec to do:
        1-move piece
        2- add to capttured set """      
        source_piece = board[source]
        dest_piece = board[destination]

        # placed in player class, since these errors would be made due to human error
        if board.isEmpty(source):
            raise ValueError("Cannot move empty square")

        if source_piece.player != self.id:
            raise ValueError("Cannot move piece that isn't yours")

        #if destination not in source_piece.possibleMoves(board):
        if destination not in type(source_piece).possibleMoves(board,source):
            raise ValueError("Invalid move")

        if not board.isEmpty(destination) and self.id == dest_piece.player:
            raise ValueError("Cannot move onto your own piece")

        #board[destination] = board[source] # place source piece in destination spot
        #board[source].update_position(destination)   # update position of source to destination
        #board[source] = None # mark source spot as empty

        source_piece.move(source,destination,board,promote)
        if dest_piece != None:
            # swap side of captured piece
            dest_piece.switchPlayers()
            self.capture(dest_piece)
            # reduce number of pieces other user has
        self.moves += 1
    
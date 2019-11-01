from utils import translate_square_coord
class Player():
    _player_id = 0
    def __init__(self):
        self._captured = set()
        self.id = Player._player_id
        self.moves = 0
        Player._player_id += 1

    def capture(self,piece):
        self._captured.add(piece)
    
    @property
    def captured(self):
        """Returns set of Piece objects"""
        return self._captured
    
    def drop(self,piece,board,square):
        square = translate_square_coord(square)
        if square in self._captured:
            self._captured.remove(piece)
            if board[(square[0],square[1])] == "":
                board[(square[0],square[1])] = piece 
            else:
                raise ValueError("Cannot drop piece on another piece")
        else:
            raise ValueError("Cannot drop non-captured piece")
    
    # returns captured piece
    def move(self,source,destination,board):
        if board[(source[0],source[1])] == None:
            raise ValueError("Cannot move empty square")
        captured_piece = board[(destination[0],destination[1])]
        
        if board[(source[0],source[1])].player != self.id:
            raise ValueError("Cannot move piece that isn't yours")

        if [destination[0],destination[1]] not in board[(source[0],source[1])].possibleMoves(board):
            print([destination[0],destination[1]])
            raise ValueError("Invalid move")

        if board[(destination[0],destination[1])] != None and self.id == captured_piece.player:
            raise ValueError("Cannot move onto your own piece")

        board[(source[0],source[1])].setposition((destination[0],destination[1]))
        board[(destination[0],destination[1])] = board[(source[0],source[1])]
        board[(source[0],source[1])] = None
        self.moves += 1
        if captured_piece != None:
            self.capture(captured_piece)
    
from utils import LOWER,UPPER,BOARD_SIZE
class Piece:
    """
    Class that represents a BoxShogi piece
    """
    # what do all pieces have in common
    # -location
    PIECE_TO_LETTER = {
        "BoxDrive": ["d","D"],
        "BoxGovernance": ["g","G"],
        "BoxNote": ["n","N"],
        "BoxShield": ["s","S"],
        "BoxRelay": ["r","R"],
        "BoxPreview": ["p","P"],
    }

    def __init__(self,row,column,player):
        # what position its in
        self._position = [row,column]
        self.player = player
        self.promoted = False
    
    def update_position(self,position):
        self._position = position

    @property
    def position(self):
        return self._position

    def __repr__(self):
        return self.PIECE_TO_LETTER[type(self).__name__][self.player]
    
    @staticmethod
    def getChar(piece):
        if piece == None:
            return ""
        char = Piece.PIECE_TO_LETTER[type(piece).__name__][piece.player]
        return f"+{char}" if piece.promoted else f"{char}"

    def switchPlayers(self):
        self.player = UPPER if self.player == LOWER else LOWER
        

    def move(self,source,destination,board,user_promote):
        dest_row = destination[0]
        src_row = source[0]
        if user_promote and ((repr(self) in Piece.PIECE_TO_LETTER["BoxDrive"] or repr(self) in Piece.PIECE_TO_LETTER["BoxShield"])):
            raise ValueError("Cannot promote BoxDrive or BoxShield")
        if user_promote and (self.promoted):
            raise ValueError("Cannot promote piece that's already promoted")

        if (user_promote or type(board[source]).__name__ == "BoxPreview") and (((dest_row == BOARD_SIZE-1 or src_row == BOARD_SIZE-1) and self.player == LOWER) or \
        ((dest_row == 0 or src_row == 0) and self.player == UPPER)):
            self.promote()
        
        dest_piece = board[destination]
        board[destination] = board[source]
        board[source] = None
        self.update_position(destination)


    def demote(self):
        self.promoted = False
    
    
    def promote(self):
        if repr(self) not in Piece.PIECE_TO_LETTER["BoxDrive"] and repr(self) not in Piece.PIECE_TO_LETTER["BoxShield"]:
            self.promoted = True
        
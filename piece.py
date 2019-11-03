from utils import LOWER,UPPER,BOARD_SIZE
class Piece:
    """
    Class that represents a BoxShogi piece
    """
    # what do all pieces have in common
    # -location
    PIECE_MAP = {
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
        # self.can_be_promoted = False
    
    def update_position(self,position):
        self._position = position

    @property
    def position(self):
        return self._position

    def __repr__(self):
        return self.PIECE_MAP[type(self).__name__][self.player]
    
    @staticmethod
    def getChar(piece):
        if piece == None:
            return ""
        char = Piece.PIECE_MAP[type(piece).__name__][piece.player]
        return f"+{char}" if piece.promoted else f"{char}"

    def switchPlayers(self):
        self.player = UPPER if self.player == LOWER else LOWER
        

    def move(self,source,destination,board,promote):
        dest_piece = board[destination]
        board[destination] = board[source]
        board[source] = None
        self.update_position(destination)
        dest_row = destination[0]
        src_row = source[0]
        print(promote)
        if promote and ((dest_row == BOARD_SIZE-1 or src_row == BOARD_SIZE-1) and self.player == LOWER) or \
        ((dest_row == 0 or src_row == 0) and self.player == UPPER):
            self.promote()

        # if not self.can_be_promoted and destination[0] == 0 and self.player == UPPER:
        #     self.can_be_promoted = True
        # elif not self.can_be_promoted and destination[0] == 4 and self.player == LOWER:
        #     self.can_be_promoted = True

        # if user passed in promoted flag:
        #   detect if source or destination are in the promo row
        #       if it is, mark item as promoted

    def demote(self):
        self.promoted = False
    
    # def promote(self):
    #     if repr(self) in PIECE_MAP["BoxDrive"] or repr(self) in PIECE_MAP["BoxShield"]:
    #         raise ValueError("Cannot promote Box Drive")
    #     self.promoted = True
    
    def promote(self):
        if repr(self) not in Piece.PIECE_MAP["BoxDrive"] and repr(self) not in Piece.PIECE_MAP["BoxShield"]:
            self.promoted = True
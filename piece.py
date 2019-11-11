from utils import LOWER,UPPER,BOARD_SIZE


class PromotionError(Exception):
    pass

class Piece:
    """
    Class that represents a BoxShogi piece
    """

    PIECE_TO_LETTER = {
        "BoxDrive": ["d","D"],
        "BoxGovernance": ["g","G"],
        "BoxNote": ["n","N"],
        "BoxShield": ["s","S"],
        "BoxRelay": ["r","R"],
        "BoxPreview": ["p","P"],
    }

    def __init__(self,row,column,player):
        self._position = [row,column]
        self.player = player
        self.promoted = False
    
    def update_position(self,position):
        self._position = position

    @property
    def position(self):
        return self._position

    def __repr__(self):
        return Piece.getChar(self)
    
    @staticmethod
    def getChar(piece):
        if piece == None:
            return ""
        char = Piece.PIECE_TO_LETTER[piece.getClassName()][piece.player]
        return f"+{char}" if piece.promoted else f"{char}"

    def switchPlayers(self):
        self.player = UPPER if self.player == LOWER else LOWER

    def getClassName(self):
        return type(self).__name__
        
    def move(self,source,destination,board,user_promote):
        DEST_ROW = destination[0]
        SRC_ROW = source[0]
        if user_promote and ((repr(self) in Piece.PIECE_TO_LETTER["BoxDrive"] or repr(self) in Piece.PIECE_TO_LETTER["BoxShield"])):
            raise PromotionError("Cannot promote BoxDrive or BoxShield")
        if user_promote and (self.promoted):
            raise PromotionError("Cannot promote piece that's already promoted")

        if (user_promote or board[source].getClassName() == "BoxPreview") and (((DEST_ROW == BOARD_SIZE-1 or SRC_ROW == BOARD_SIZE-1) and self.player == LOWER) or \
        ((DEST_ROW == 0 or SRC_ROW == 0) and self.player == UPPER)):
            self.promote()
        
        # move piece on board
        board[destination] = board[source]
        board[source] = None
        self.update_position(destination)


    def demote(self):
        self.promoted = False
    
    
    def promote(self):
        if repr(self) not in Piece.PIECE_TO_LETTER["BoxDrive"] and repr(self) not in Piece.PIECE_TO_LETTER["BoxShield"]:
            self.promoted = True
        else:
            raise PromotionError("Cannot promote BoxDrive or BoxShield pieces")
        
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
        '''Updates position of piece'''
        self._position = position

    @property
    def position(self) -> tuple:
        return self._position

    def __repr__(self):
        return Piece.getChar(self)
    
    @staticmethod
    def getChar(piece) -> str:
        '''Returns character representation of piece on board'''
        if piece == None:
            return ""
        char = Piece.PIECE_TO_LETTER[piece.getClassName()][piece.player]
        return f"+{char}" if piece.promoted else f"{char}"

    def switchPlayers(self):
        '''Swap players (used for when piece is captured) '''
        self.player = UPPER if self.player == LOWER else LOWER

    def getClassName(self) -> str:
        '''Returns class name of piece objet '''
        return type(self).__name__
    
    def _validatePromotion(self,board,source,user_promote,dest_row,src_row):
        '''Validates whether move can be made given what kind of piece it is '''
        if user_promote and ((repr(self) in Piece.PIECE_TO_LETTER["BoxDrive"] or repr(self) in Piece.PIECE_TO_LETTER["BoxShield"])):
            raise PromotionError("Cannot promote BoxDrive or BoxShield")
        if user_promote and (self.promoted):
            raise PromotionError("Cannot promote piece that's already promoted")
            
        if (user_promote or board[source].getClassName() == "BoxPreview") and \
        (((dest_row == BOARD_SIZE-1 or src_row == BOARD_SIZE-1) and self.player == LOWER) or \
        ((dest_row == 0 or src_row == 0) and self.player == UPPER)):
            self.promote()

    def move(self,source,destination,board,user_promote):
        '''Moves piece on board and cleans old position to be blank'''
        DEST_ROW = destination[0]
        SRC_ROW = source[0]
        self._validatePromotion(board,source,user_promote,DEST_ROW,SRC_ROW)
        
        # move piece on board
        board[destination] = board[source]
        board[source] = None
        self.update_position(destination)


    def demote(self):
        '''Demotes piece (used when piece is captured)'''
        self.promoted = False
    
    
    def promote(self):
        '''Promotes piece, provided it is not a BoxDrive or BoxShield'''
        if repr(self) not in Piece.PIECE_TO_LETTER["BoxDrive"] and repr(self) not in Piece.PIECE_TO_LETTER["BoxShield"]:
            self.promoted = True
        else:
            raise PromotionError("Cannot promote BoxDrive or BoxShield pieces")
        
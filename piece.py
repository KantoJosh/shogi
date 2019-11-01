from utils import LOWER,UPPER
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
    
    def setposition(self,position):
        self._position = [position[0],position[1]]

    @property
    def position(self):
        return self._position

    def __repr__(self):
        char = self.PIECE_MAP[type(self).__name__][self.player]
        return f"{char}"
    
    @staticmethod
    def getChar(piece):
        if piece == None:
            return ""
        return Piece.PIECE_MAP[type(piece).__name__][piece.player]

    def switchPlayers(self):
        self.player = UPPER if self.player == LOWER else LOWER
        

    def move(self,source,destination,board):
        s_x,s_y = source
        d_x,d_y = destination
        if board[(s_x,s_y)] == None:
            raise ValueError("Cannot move empty square")
        captured_piece = board[(d_x,d_y)]
        board[(d_x,d_y)] = board[(s_x,s_y)]
        board[(s_x,s_y)] = None
        #self.setposition(destination)
        return captured_piece

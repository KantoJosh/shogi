class Piece:
    """
    Class that represents a BoxShogi piece
    """
    # what do all pieces have in common
    # -location
    PIECE_MAP = {
        "BoxDrive": "d",
        "BoxGovernance": "g",
        "BoxNote": "n",
        "BoxShield": "s",
        "BoxRelay": "r",
        "BoxPreview": "p",
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
        char = self.PIECE_MAP[type(self).__name__]
        return f"{char.lower() if self.player == 0 else char.upper()}"

    def move(self,source,destination,board):
        if board[(source[0],source[1])] == None:
            raise ValueError("Cannot move empty square")
        captured_piece = board[(destination[0],destination[1])]
        board[(destination[0],destination[1])] = board[(source[0],source[1])]
        board[(source[0],source[1])] = None
        #self.setposition(destination)
        return captured_piece

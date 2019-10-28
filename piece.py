class Piece:
    """
    Class that represents a BoxShogi piece
    """
    # what do all pieces have in common
    # -location

    def __init__(self,row,column):
        # what position its in
        self._position = [row,column]
    
    @property
    def position(self):
        return self._position

    def __repr__(self):
        return f"{type(self).__name__} at {self._position}"

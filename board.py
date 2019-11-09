import os
from utils import BOARD_SIZE,LOWER,UPPER,translate_square_coord
from piece import Piece
from boxgov import BoxGovernance
from boxdrive import BoxDrive
from boxnote import BoxNote
from boxpreview import BoxPreview
from boxrelay import BoxRelay
from boxshield import BoxShield
class Board:
    """
    Class that represents the BoxShogi board
    """
    letter_to_piece = {
        "d" : BoxDrive,
        "n" : BoxNote,
        "g" : BoxGovernance,
        "s" : BoxShield,
        "r" : BoxRelay,
        "p" : BoxPreview,
    }

    # The BoxShogi board is 5x5
    BOARD_SIZE = 5
    def __init__(self):
        self._board = self._initEmptyBoard() # backend representation of board

    def _initEmptyBoard(self):
        # TODO: Initalize empty board
        return [[None]*5 for _ in range(Board.BOARD_SIZE)]
    
    def _initStartBoard(self):
        self._board[4] = [BoxNote(4,0,UPPER),BoxGovernance(4,1,UPPER),BoxRelay(4,2,UPPER),BoxShield(4,3,UPPER),BoxDrive(4,4,UPPER)]
        self._board[0] = [BoxDrive(0,0,LOWER),BoxShield(0,1,LOWER),BoxRelay(0,2,LOWER),BoxGovernance(0,3,LOWER),BoxNote(0,4,LOWER)]
        self._board[1][0] = BoxPreview(1,0,LOWER)
        self._board[3][4] = BoxPreview(3,4,UPPER)
    
    def _initBoardFromFile(self,data,lower,upper):
        # place pieces onto board
        for initialPiece in data['initialPieces']:
            row,col = translate_square_coord(initialPiece['position'])
            player = LOWER if initialPiece['piece'][-1].lower() == initialPiece['piece'][-1] else UPPER
            piece = self.letter_to_piece[initialPiece['piece'][-1].lower()](row,col,player)
            if len(initialPiece['piece']) > 1:
                piece.promote() # piece is promoted
            self._board[row][col] = piece 
        
        for piece in data['upperCaptures']:
            piece = self.letter_to_piece[piece.lower()](None,None,UPPER)
            upper.capture(piece)

        for piece in data['lowerCaptures']:
            piece = self.letter_to_piece[piece.lower()](None,None,LOWER) 
            lower.capture(piece)
    
    def isEmpty(self,coordinate):
        return self[(coordinate[0],coordinate[1])] == None

    def __repr__(self):
        return self._stringifyBoard()

    # def getPieceChar(self,piece):
    #     if piece == None:
    #         return ""
    #     return Piece.PIECE_TO_LETTER[type(piece).__name__][piece.player]

    def _stringifyBoard(self):
        """
        Utility function for printing the board
        """
        s = ''
        for row in range(len(self._board) - 1, -1, -1):

            s += '' + str(row + 1) + ' |'
            for col in range(0, len(self._board[row])):
                s += self._stringifySquare(Piece.getChar(self._board[row][col]))

            s += os.linesep

        s += '    a  b  c  d  e' + os.linesep
        return s

    def __getitem__(self,coord):
        return self._board[coord[0]][coord[1]]
    
    def __setitem__(self,coord,piece):
        self._board[coord[0]][coord[1]] = piece


    def _stringifySquare(self, sq):
        """
       	Utility function for stringifying an individual square on the board

        :param sq: Array of strings.
        """
        if type(sq) is not str or len(sq) > 2:
            raise ValueError('Board must be an array of strings like "", "P", or "+P"')
        if len(sq) == 0:
            return '__|'
        if len(sq) == 1:
            return ' ' + sq + '|'
        if len(sq) == 2: # promoted
            return sq + '|'
    


import os
from utils import BOARD_SIZE
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
    # The BoxShogi board is 5x5
    BOARD_SIZE = 5
    def __init__(self):
        self._board = self._initEmptyBoard() # backend representation of board

    def _initEmptyBoard(self):
        # TODO: Initalize empty board
        return [[None]*5 for _ in range(Board.BOARD_SIZE)]
    
    def _initStartBoard(self):
        self._board[4] = [BoxNote(4,0,1),BoxGovernance(4,1,1),BoxRelay(4,2,1),BoxShield(4,3,1),BoxDrive(4,4,1)]
        self._board[0] = [BoxDrive(0,0,0),BoxShield(0,1,0),BoxRelay(0,2,0),BoxGovernance(0,3,0),BoxNote(0,4,0)]
        self._board[1][0] = BoxPreview(1,0,0)
        self._board[3][4] = BoxPreview(3,4,1)
    
    def isEmpty(self,coordinate):
        return self[(coordinate[0],coordinate[1])] == None

    def __repr__(self):
        return self._stringifyBoard()

    # def getPieceChar(self,piece):
    #     if piece == None:
    #         return ""
    #     return Piece.PIECE_MAP[type(piece).__name__][piece.player]

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
    


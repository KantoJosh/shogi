from utils import translate_square_coord,LOWER,UPPER
from piece import Piece
from boxdrive import BoxDrive
from copy import deepcopy
# 

class Player():
    _player_id = 0
    def __init__(self):
        self._captured = []
        # self._captured = {
        #     "d": [],
        #     "g": [],
        #     "n" : [],
        #     "s" : [],
        #     "r" : [],
        #     "p" : []
        # }
        self.id = Player._player_id
        self.moves = 0
        self.in_check = False
        self.king_loc = None
        Player._player_id += 1

    def capture(self,piece):
        if piece == None:
            raise ValueError("Cannot capture empty square")
        piece.demote()
        self._captured.append(piece)
        #self._captured[Piece.getChar(piece).lower()].append(piece)

    
    def free(self,key):
        # if key not in self._captured.keys():
        #     raise ValueError("Invalid piece was attempted to be dropped")
        # if len(self._captured[key]) == 0:
        #     raise ValueError("Can not remove nonexistent piece from captured set")
        # return self._captured[key].pop() 
        for p in range(len(self._captured)):
            if Piece.getChar(self._captured[p]).lower() == key:
                return self._captured.pop(p)
        else:
            raise ValueError("Invalid piece was attempted to be dropped")

    
    @property
    def captured(self):
        """Returns set of Piece objects"""
        return self._captured
    
    def drop(self,pieceChar,board,destination,opponent):
        # scan column for box preview
        x,y = destination
        if pieceChar == "p" or pieceChar == "P":
            # check if box preview in same column
            for row in range(board.BOARD_SIZE):
                if repr(board[(row,y)]) in ["P","p"] and board[(row,y)].player == self.id: 
                    raise ValueError("Cannot drop box preview in same column as another")

        if not board.isEmpty(destination): 
            raise ValueError("Cannot drop piece on another piece")
        in_promo_zone = (destination[0] == 0 and self.id == UPPER) or (destination[0] == board.BOARD_SIZE-1 and self.id == LOWER) 


        if pieceChar == "p" and in_promo_zone: 
            raise ValueError("Cannot drop BoxPreview in promotion zone")
        elif pieceChar == "p" and False: # eventually change False to is_in_checkmate (immediate as of moving to destination)
            pass

        piece = self._captured[0]

        if type(piece).__name__ == "BoxPreview":
            board_copy = deepcopy(board)
            board_copy[destination] = piece
            opponent_copy = deepcopy(opponent)
            if len(opponent_copy.checkmate(board_copy)) == 0: 
                raise ValueError("Cannot drop Box Preview to cause immediate checkmate")

        piece = self.free(pieceChar)
        piece.update_position(destination)
        board[destination] = piece 

    # def checkmate(self,board):
    #     king_moves  = set(BoxDrive.possibleMoves(board,self.king_loc)) # list of tuples
    #     new_moves = set()
    #     for move in king_moves:
    #         board_copy = deepcopy(board)
    #         self.move(self.king_loc,move,board_copy,False,False)
    #         if not self.check(board_copy,move):
    #             new_moves.add(move)
    #     return new_moves

    def move(self,source,destination,board,promote,undo_king = True):  
        """Concerns with player's move: what they neec to do:
        1-move piece
        2- add to capttured set """      
        source_piece = board[source]
        dest_piece = board[destination]

        # placed in player class, since these errors would be made due to human error
        if board.isEmpty(source):
            raise ValueError("Cannot move empty square")

        if source_piece.player != self.id:
            raise ValueError("Cannot move piece that isn't yours")

        #if destination not in source_piece.possibleMoves(board):
        if destination not in type(source_piece).possibleMoves(board,source):
            raise ValueError("Invalid move")

        if not board.isEmpty(destination) and self.id == dest_piece.player:
            raise ValueError("Cannot move onto your own piece")

        if type(board[source]).__name__ == "BoxDrive":
            if not self.check(board,source):
                board_copy = deepcopy(board)
                source_piece.move(source,destination,board_copy,False)
                if self.check(board_copy,destination):
                    raise ValueError("Cannot move into check")


        source_piece.move(source,destination,board,promote)
        if type(source_piece).__name__ == "BoxDrive" and undo_king:
            self.king_loc = destination

        if dest_piece != None:
            # swap side of captured piece
            dest_piece.switchPlayers()
            self.capture(dest_piece)
            # reduce number of pieces other user has
        self.moves += 1

    def check(self,board,king_pos = None):
        if king_pos == None:
            king_pos = self.king_loc
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
                # not empty, enemy player, and possible moves contain self.king_loc
                if board[(i,j)] != None and board[(i,j)].player != self.id and king_pos in type(board[(i,j)]).possibleMoves(board,(i,j)):
                    return True
        return False
    
    def findEscapeMoves(self,board):
        king_moves  = set(BoxDrive.possibleMoves(board,self.king_loc)) # list of tuples

        #print("KING",king_moves)
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
                if board[(i,j)] != None and board[(i,j)].player != self.id:
                    opponent_moves = type(board[(i,j)]).possibleMoves(board,(i,j))
                    #print("OPP",type(board[(i,j)]).__name__,opponent_moves)
                    bannedMoves = list(set(king_moves) & set(opponent_moves))
                    for b in bannedMoves:
                        if b in king_moves:
                            king_moves.remove(b)
                            break
        return king_moves



    def checkmate(self,board):
        king_moves  = set(BoxDrive.possibleMoves(board,self.king_loc)) # list of tuples
        new_moves = set()
        for move in king_moves:
            board_copy = deepcopy(board)
            self.move(self.king_loc,move,board_copy,False,False)
            if not self.check(board_copy,move):
                new_moves.add(move)
        return new_moves





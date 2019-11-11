from utils import translate_square_coord,LOWER,UPPER
from piece import Piece
from boxdrive import BoxDrive
from copy import deepcopy
from collections import defaultdict
# 
class PlayerError(Exception):
    pass

class IllegalDrop(PlayerError):
    pass

class IllegalMove(PlayerError):
    pass

class Player():
    _player_id = 0
    def __init__(self):
        self._captured = []
        self.player = Player._player_id
        self.moves = 0
        self.in_check = False
        self.king_loc = None
        Player._player_id += 1

    def capture(self,piece):
        if piece == None:
            raise IllegalMove("Cannot capture empty square")
        piece.demote()
        self._captured.append(piece)

    
    def free(self,key):
        for p in range(len(self._captured)):
            if Piece.getChar(self._captured[p]).lower() == key.lower():
                return self._captured.pop(p)
        else:
            raise IllegalDrop("Invalid piece was attempted to be dropped")

    
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
                if repr(board[(row,y)]) in ["P","p"] and board[(row,y)].player == self.player: 
                    raise IllegalDrop("Cannot drop box preview in same column as another")

        if not board.isEmptyAt(destination): 
            raise IllegalDrop("Cannot drop piece on another piece")
        in_promo_zone = (destination[0] == 0 and self.player == UPPER) or (destination[0] == board.BOARD_SIZE-1 and self.player == LOWER) 


        if pieceChar == "p" and in_promo_zone: 
            raise IllegalDrop("Cannot drop BoxPreview in promotion zone")

        if len(self.captured) > 0:
            piece = self._captured[0]
        else:
            raise IllegalDrop("Cannot drop piece from empty captured set")

        if piece.getClassName() == "BoxPreview":
            board_copy = deepcopy(board)
            board_copy[destination] = piece
            opponent_copy = deepcopy(opponent) # copied so no affect on captured set
            if len(opponent_copy.checkmate(board_copy)) == 0: 
                raise IllegalDrop("Cannot drop Box Preview to cause immediate checkmate")

        piece = self.free(pieceChar)
        piece.update_position(destination)
        board[destination] = piece 


    def move(self,source,destination,board,promote,update_king_loc = True):  
        """Concerns with player's move: what they neec to do:"""      
        source_piece = board[source]
        dest_piece = board[destination]

        if board.isEmptyAt(source):
            raise IllegalMove("Cannot move empty square")

        if source_piece.player != self.player:
            raise IllegalMove("Cannot move piece that isn't yours")

        if destination not in type(source_piece).possibleMoves(board,source):
            raise IllegalMove("Invalid move")

        if not board.isEmptyAt(destination) and self.player == dest_piece.player:
            raise IllegalMove("Cannot move onto your own piece")

        if board[source].getClassName() == "BoxDrive":
            if not self.check(board,source):
                board_copy = deepcopy(board)
                source_piece.move(source,destination,board_copy,False)
                if self.check(board_copy,destination):
                    raise IllegalMove("Cannot move into check")


        source_piece.move(source,destination,board,promote)
        if source_piece.getClassName() == "BoxDrive" and update_king_loc:
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
                if board[(i,j)] != None and board[(i,j)].player != self.player and king_pos in type(board[(i,j)]).possibleMoves(board,(i,j)):
                    return True
        return False
    

    def checkmate(self,board):
        king_moves  = set(BoxDrive.possibleMoves(board,self.king_loc)) # list of tuples
        new_moves = set()
        for move in king_moves:
            board_copy = deepcopy(board)
            self.move(self.king_loc,move,board_copy,False,False)
            if not self.check(board_copy,move):
                new_moves.add(move)
        return new_moves

    def findEscapeMoves(self,board,opponent):
        king_moves = {}
        for c in BoxDrive.possibleMoves(board,self.king_loc):
            board_copy = deepcopy(board)
            self.move(self.king_loc,c,board_copy,False,False)
            if not self.check(board_copy,c):
                king_moves[c] = self.king_loc
        bannedMoves = set()
        team_moves = {}
        drop_moves = set()
        in_check = self.check(board)
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE): # traverse through board
                if not board.isEmptyAt((i,j)):
                    if board[(i,j)].player != self.player:
                        bannedMoves.update(type(board[(i,j)]).possibleMoves(board,(i,j)))
                    elif (i,j) != self.king_loc:
                        teammate_moves = type(board[(i,j)]).possibleMoves(board,(i,j))
                        for move in teammate_moves:
                            board_copy = deepcopy(board)
                            board_copy[(i,j)].move((i,j),move,board_copy,False)
                            if not self.check(board_copy,self.king_loc):
                                team_moves[move] = (i,j)
                else:
                    player_copy = deepcopy(self)
                    opponent_copy = deepcopy(opponent)
                    for c in range(len(self.captured)):
                        player_copy = deepcopy(self)
                        board_copy = deepcopy(board)
                        try:
                            player_copy.drop(Piece.getChar(self.captured[c]),board_copy,(i,j),opponent_copy)
                        except (IllegalMove,IllegalDrop):
                            pass
                        if not self.check(board_copy,self.king_loc):
                            drop_moves.add((self.captured[c],i,j))
                    # player_copy = deepcopy(self)
                    # for c in self.captured:
                    #     board_copy = deepcopy(board)
                    #     player_copy.drop(Piece.getChar(c),board_copy,(i,j),opponent_copy)
                    #     if not self.check(board_copy,self.king_loc):
                    #         drop_moves.add((self.captured[c],i,j))
                        


        for banned in bannedMoves:
            if banned in king_moves:
                del king_moves[banned]
            

        return (drop_moves,{**king_moves,**team_moves,})

from utils import parseTestCase,LOWER,UPPER,translate_square_coord,translate_letter_coord
from board import Board
from player import Player,PlayerError
import sys
from piece import PromotionError
class Game:
    MOVE_LIMIT = 200
    def __init__(self,mode = 'f',filepath = None):
        '''2 possible modes:
            -i: interactive
            -f: file mode '''
        self.data = None
        self.board = Board()
        self.players = [Player(),Player()] # 0 is lower, 1 is upper
        if mode == 'i':
            pass
        elif mode == 'f':
            if filepath == None:
                raise ValueError("Cant use file mode without file path input")
            self.data = parseTestCase(filepath)
            self.board.initBoardFromFile(self.data,self.players[LOWER],self.players[UPPER])
    
    def displayBoardState(self,turn,action):
        if turn == LOWER:
            print(f"lower player action: {' '.join(action)}")
        elif turn == UPPER:
            print(f"UPPER player action: {' '.join(action)}")
        print(repr(self.board))
        print("Captures UPPER: ",end = "")
        for c in self.players[UPPER].captured:
            print(f"{c}",end = " ")
        print()
        print("Captures lower: ",end = "")
        for c in self.players[LOWER].captured:
            print(f"{c}",end = " ")
        print("\n")
        if turn == LOWER:
            print("UPPER player wins.  Illegal move.")
        else:
            print("lower player wins.  Illegal move.")

    def boot(self):
        GAME_OVER = False
        TIE_GAME = False
        CHECK = False
        turn = LOWER
        i = 0
        moves = [d.split(" ") for d in self.data['moves']]
        while(i < len(moves) and not GAME_OVER):
            # perform check here
            # if check,set flag and exit loop
            #CHECK = self.players[turn].check(self.board)
            #if CHECK and len(self.players[turn].findEscapeMoves(self.board)) == 0:

            #king_escape_moves = self.players[turn].check(board)
            if moves[i][0] == "move":
                promote = (len(moves[i]) == 4 and moves[i][3] == "promote")
                _from, _to = moves[i][1],moves[i][2]

                from_coord = translate_square_coord(_from)        
                to_coord = translate_square_coord(_to)
                try:
                    self.players[turn].move(from_coord,to_coord,self.board,promote)
                except (PlayerError,PromotionError):
                    self.displayBoardState(turn,moves[i])
                    return 
            elif moves[i][0] == "drop":
                piece,to = moves[i][1],moves[i][2] 
                to_coord = translate_square_coord(to)
                try:
                    self.players[turn].drop(piece,self.board,to_coord,self.players[turn^1])
                except (PlayerError,PromotionError):
                    self.displayBoardState(turn,moves[i])
                    return
            else:
                raise ValueError("Invalid move format")

            if self.players[LOWER].moves == Game.MOVE_LIMIT and self.players[UPPER].moves == Game.MOVE_LIMIT:
                GAME_OVER = True
                TIE_GAME = True 
            if (i+1) >= len(moves):
                break
            turn ^= 1 
            i += 1

        if turn == LOWER:
            print(f"lower player action: {' '.join(moves[i])}")
        elif turn == UPPER:
            print(f"UPPER player action: {' '.join(moves[i])}")
        print(repr(self.board))
        print("Captures UPPER: ",end = "")
        for c in self.players[UPPER].captured:
            print(f"{c}",end = " ")

        print()
        print("Captures lower: ",end = "")
        for c in self.players[LOWER].captured:
            print(f"{c}",end = " ")
        print("\n")
        if TIE_GAME:
            print("Tie game.  Too many moves.")
            return

        if self.players[turn ^ 1].check(self.board):
            escape = sorted(self.players[turn ^ 1].checkmate(self.board),key = lambda coord: (coord[1],coord[0]))
            drop_escape,esc = self.players[turn ^ 1].findEscapeMoves(self.board,self.players[turn])
            if len(escape) == 0:
                if (turn^1) == LOWER:
                    print("UPPER player wins.  Checkmate.")
                else:
                    print("lower player wins.  Checkmate.")
                return 
            else:
                if turn == UPPER:
                    print("lower player is in check!")
                else:
                    print("UPPER player is in check!")

            print("Available moves:")
            for d_esc in sorted(drop_escape,key = lambda x: (repr(x[0]),x[1],x[2])):
                piece = d_esc[0]
                col = translate_letter_coord((d_esc[1],d_esc[2]))
                print(f"drop {repr(piece).lower()} {col}")
            for dest in sorted(esc,key = lambda dest: (translate_letter_coord(esc[dest]),translate_letter_coord(dest))):
                _to = translate_letter_coord(dest)
                _from = translate_letter_coord(esc[dest])
                print(f"move {_from} {_to}")
                
            
            # for esc in escape:
            #     king_coord = translate_letter_coord(self.players[turn ^ 1].king_loc)
            #     letter_coord = translate_letter_coord(esc)
            #     print(f"move {king_coord} {letter_coord}")

        if turn == LOWER:
            print("UPPER>")
        else:
            print("lower>")


if __name__ == "__main__":
    filepath = None 
    arg_length = len(sys.argv)
    if arg_length > 2:
        filepath = sys.argv[2]
    game = Game('f',filepath)
    game.boot()
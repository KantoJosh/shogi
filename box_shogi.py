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
        if mode == '-i':
            self.board.initInteractiveBoard()
            self.boot_interactive()
        elif mode == '-f':
            if filepath == None:
                raise ValueError("Cant use file mode without file path input")
            self.data = parseTestCase(filepath)
            self.board.initBoardFromFile(self.data,self.players[LOWER],self.players[UPPER])
            self.boot_file()
    
    def displayBoardState(self,turn,action):
        '''Displays state of board and actions/captures '''
        if turn == LOWER:
            print(f"lower player action: {' '.join(action)}")
        elif turn == UPPER:
            print(f"UPPER player action: {' '.join(action)}")
        print(repr(self.board))
        self._displayCaptures()
        if turn == LOWER:
            print("UPPER player wins.  Illegal move.")
        else:
            print("lower player wins.  Illegal move.")
    
    def _displayCaptures(self):
        print("Captures UPPER: ",end = "")
        for c in self.players[UPPER].captured:
            print(f"{c}",end = " ")
        print()
        print("Captures lower: ",end = "")
        for c in self.players[LOWER].captured:
            print(f"{c}",end = " ")
        print("\n")

    def check_clause(self,turn):
            '''Prints layout for check, if the function needs to exit (due to checkmate),
            True will be returned '''
            if self.players[turn ^ 1].check(self.board):
                escape = sorted(self.players[turn ^ 1].checkmate(self.board),key = lambda coord: (coord[1],coord[0]))
                drop_escape,esc = self.players[turn ^ 1].findEscapeMoves(self.board,self.players[turn])
                if len(escape) == 0:
                    if (turn^1) == LOWER:
                        print("UPPER player wins.  Checkmate.")
                    else:
                        print("lower player wins.  Checkmate.")
                    return True
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

    def _displayPlayerAction(self,turn,action):
        if turn == LOWER:
            print(f"lower player action: {' '.join(action)}")
        elif turn == UPPER:
            print(f"UPPER player action: {' '.join(action)}")
        
    def _displayPlayerTurn(self,turn):
        if turn == LOWER:
            print("UPPER>")
        else:
            print("lower>")

    def boot_file(self):
        '''Boots game from filepath specified during initialization '''
        GAME_OVER = False
        TIE_GAME = False
        CHECK = False
        turn = LOWER
        i = 0
        moves = [d.split(" ") for d in self.data['moves']]
        while(i < len(moves) and not GAME_OVER):
            if self.check_clause(turn):
                return
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
            turn ^= 1 # switch turns when last turn is over
            i += 1 # increment move counter


        self._displayPlayerAction(turn,moves[i])
        print(repr(self.board))
        print("Captures UPPER: ",end = "")
        for c in self.players[UPPER].captured:
            print(f"{c}",end = " ")

        print("\nCaptures lower: ",end = "")
        for c in self.players[LOWER].captured:
            print(f"{c}",end = " ")
        print("\n")
        
        if TIE_GAME:
            print("Tie game.  Too many moves.")
            return

        if self.check_clause(turn):
            return

        self._displayPlayerTurn(turn)
    
    def boot_interactive(self):
        GAME_OVER = False
        TIE_GAME = False
        turn = LOWER
        while (not GAME_OVER):
            print(repr(self.board))
            self._displayCaptures()

            prompt = "lower> " if turn == 0 else "UPPER> "
            action_input = input(f"\n{prompt}").split(" ")
            if action_input[0] == "move":
                promote = (len(action_input) == 4 and action_input[3] == "promote")
                _from, _to = action_input[1],action_input[2]

                from_coord = translate_square_coord(_from)        
                to_coord = translate_square_coord(_to)
                try:
                    self.players[turn].move(from_coord,to_coord,self.board,promote)
                except (PlayerError,PromotionError):
                    self.displayBoardState(turn,moves[i])
                    return
                    

                
            elif action_input[0] == "drop":
                piece,to = action_input[1],action_input[2] 
                to_coord = translate_square_coord(to)
                try:
                    self.players[turn].drop(piece,self.board,to_coord)
                except (PlayerError,PromotionError):
                    self.displayBoardState(turn,moves[i])
                    return
            else:
                raise ValueError("Invalid move format")

            self._displayPlayerAction(turn,action_input)
            
            turn ^= 1 
            if self.players[LOWER].moves == Game.MOVE_LIMIT and self.players[UPPER].moves == Game.MOVE_LIMIT:
                GAME_OVER = True
                TIE_GAME = True 
            
        if TIE_GAME:
            print("Tie game. Too many moves")





if __name__ == "__main__":
    filepath = None 
    arg_length = len(sys.argv)
    if arg_length >= 2:
        mode = sys.argv[1]
    if arg_length > 2:
        filepath = sys.argv[2]
    game = Game(mode,filepath)
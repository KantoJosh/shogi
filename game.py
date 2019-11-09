from utils import parseTestCase,LOWER,UPPER,translate_square_coord
from board import Board
from player import Player
import sys
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
            self.board._initBoardFromFile(self.data,self.players[LOWER],self.players[UPPER])
        
    def boot(self):
        GAME_OVER = False
        TIE_GAME = False
        turn = LOWER
        i = 0
        moves = [x.split(" ") for x in self.data['moves']]
        while(i < len(moves) and not GAME_OVER):
            #print(repr(self.board))
            if moves[i][0] == "move":
                promote = (len(moves[i]) == 4 and moves[i][3] == "promote")
                _from, _to = moves[i][1],moves[i][2]

                from_coord = translate_square_coord(_from)        
                to_coord = translate_square_coord(_to)
                try:
                    self.players[turn].move(from_coord,to_coord,self.board,promote)
                except:
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
                    if turn == LOWER:
                        print("UPPER player wins.  Illegal move.")
                    else:
                        print("lower player wins.  Illegal move.")
                    return 
            elif moves[i][0] == "drop":
                piece,to = moves[i][1],moves[i][2] 
                to_coord = translate_square_coord(to)
                try:
                    self.players[turn].drop(piece,self.board,to_coord)
                except:
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

                    if turn == LOWER:
                        print("UPPER player wins.  Illegal move.")
                    else:
                        print("lower player wins.  Illegal move.")
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
        #print(f"Captures UPPER {self.players[UPPER].captured}")
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
        #print(f"Captures lower {self.players[LOWER].captured}")

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
from player import Player
from board import Board
from utils import translate_square_coord,LOWER,UPPER

MOVE_LIMIT = 200
def main():
    GAME_OVER = False
    TIE_GAME = False
    # create both players here
    players = [Player(),Player()] # 0 is lower, 1 is upper
    board = Board() # backend board
    board.initInteractiveBoard()
    turn = LOWER
    while(not GAME_OVER):

        # print board state
        print(repr(board))
        
        # print captures
        print(f"Captures UPPER {players[UPPER].captured}")
        print(f"Captures lower {players[LOWER].captured}")

        # prompt for input 
        prompt = "lower> " if turn == 0 else "UPPER> "
        action_input = input(f"\n{prompt}").split(" ")
        # process input
        if action_input[0] == "move":
            promote = (len(action_input) == 4 and action_input[3] == "promote")
            _from, _to = action_input[1],action_input[2]

            from_coord = translate_square_coord(_from)        
            to_coord = translate_square_coord(_to)

            players[turn].move(from_coord,to_coord,board,promote)

            
        elif action_input[0] == "drop":
            piece,to = action_input[1],action_input[2] 
            to_coord = translate_square_coord(to)
            players[turn].drop(piece,board,to_coord)
            pass
        else:
            raise ValueError("Invalid move format")

        if turn == LOWER:
            print(f"lower player action: {' '.join(action_input)}")
        elif turn == UPPER:
            print(f"UPPER player action: {' '.join(action_input)}")


        turn ^= 1 
        if players[LOWER].moves == MOVE_LIMIT and players[UPPER].moves == MOVE_LIMIT:
            GAME_OVER = True
            TIE_GAME = True 

    if TIE_GAME:
        print("Tie game. Too many moves")
             

if __name__ == "__main__":
    main()

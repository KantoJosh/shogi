from player import Player
from board import Board
from utils import translate_square_coord,LOWER,UPPER
GAME_OVER = False

# create both players here
players = [Player(),Player()] # 0 is lower, 1 is upper
board = Board() # backend board
board._initStartBoard()
turn = 0
while(not GAME_OVER):

    # print board state
    print(repr(board))
    
    # print captures
    print(f"Captures UPPER {players[UPPER].captured}")
    print(f"Captures lower {players[LOWER].captured}")

    # prompt for input 
    prompt = "lower> " if turn == 0 else "UPPER> "
    action_input = input(prompt).split(" ")
    # process input
    if action_input[0] == "move":
        promote = (len(action_input) == 4 and action[3] == "promote")
        _from, _to = action_input[1],action_input[2]

        from_coord = translate_square_coord(_from)        
        to_coord = translate_square_coord(_to)
        
        players[turn].move(from_coord,to_coord,board)
    elif action == "drop":
        piece,to = action[1],action[2] 
    else:
        raise ValueError("Invalid move")

    if turn == LOWER:
        print(f"lower player action: {' '.join(action_input)}")
    elif turn == UPPER:
        print(f"UPPER player action: {' '.join(action_input)}")


    turn ^= 1 
    if players[0].moves == 200 and players[1].moves == 200:
        GAME_OVER = True
        print("Tie game. Too many moves")

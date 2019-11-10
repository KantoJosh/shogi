LOWER = 0
UPPER = 1
BOARD_SIZE = 5

def parseTestCase(path):
    """
    Utility function to help parse test cases.
    :param path: Path to test case file.
    """
    f = open(path)
    line = f.readline()
    initialBoardState = []
    while line != '\n':
        piece, position = line.strip().split(' ')
        initialBoardState.append(dict(piece=piece, position=position))
        line = f.readline()
    line = f.readline().strip()
    upperCaptures = [x for x in line[1:-1].split(' ') if x != '']
    line = f.readline().strip()
    lowerCaptures = [x for x in line[1:-1].split(' ') if x != '']
    line = f.readline()
    line = f.readline()
    moves = []
    while line != '':
        moves.append(line.strip())
        line = f.readline()

    return dict(initialPieces=initialBoardState, upperCaptures=upperCaptures, lowerCaptures=lowerCaptures, moves=moves)

letter_map = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3,
        "e" : 4
    }

number_map = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e"
}

def translate_letter_coord(coordinate):
    x,y = coordinate # 1 0  ---> 0 = a ///// 1 == 1 ===> a1
    letter = number_map[y]
    number = x

    return f"{letter}{number+1}"

def translate_square_coord(coordinate):
    letter = coordinate[0]
    column = letter_map[letter]
    row = abs(int(coordinate[1]) - 1)
    return (row,column)


if __name__ == "__main__":
    # test translate_square_coord
    test1 = translate_square_coord("a2")
    assert(translate_square_coord("a2") == (1,0))
    assert(translate_square_coord("b4") == (3,1))
    assert(translate_square_coord("e5") == (4,4))

    x = parseTestCase("/BoxShogi Test Cases/basicCheck.in")




# 5 | N| G| R| S| D|
# 4 |__|__|__|__| P|
# 3 |__|__|__|__|__|
# 2 | p|__|__|__|__|
# 1 | d| s| r| g| n|
#     a  b  c  d  e
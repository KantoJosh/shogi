# notes 
how to detect if you are in check:
    - during oponnent's turn check if any of the possible moves 
how to detect if you are in check:
    - store king position
    - check if all possible moves for each enemy piece contains the king position

how to detect if you are in checkmate:
    A- keep track of coordinate of box drive and check whether its in possiblemoves of piece that will be moved

issues
    -fix dropping box preview in another col containing box preview

extras
    -convert possible moves to set


check:
    iterate through board and see if any pieces possible moves include kings location
    if so,break and return true

    then 
    iterate through board and see if any pieces map to possible moves of king. remove each move from kings possible 
    moves that is found. if end list is empty, checkmate, end game, else present the remainder of the list is possible moves


    in check either in player
    player will contain var holding king_loc
    call in check before turn pass in board- iterate thru board, and check if king loc is inside any piece


# TODO
 make possibleMoves into set

 # checkmate
 get all possible moves of king
    iterate through each move and do that move and check if king is still in check
    if it is, remove that move from possible moves
    else
    keep in list
    then undo the move (either by creating a copy of the old board every time, or undoing the move)
 if that list is empty, you're in checkmate


 immediatePreviewDropMate ----- prevent box preview from being dropped and causing checkmate:
 how? -> if piece is box preview, simulate drop at location requested on a copied board and see if opponent is in checkmate: if so, raise error
 manyWaysOutOfCheck --> simulate every move of each piece on your team. if one of them causes no check, add that as a move to possible moves
 movingIntoCheck ---- prevent from moving into check by simulating move and seeing if it causes check

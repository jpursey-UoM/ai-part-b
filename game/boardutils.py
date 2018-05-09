# create a new (empty) board (2d list)
def new_board():
    board_len = 8
    board = []
    for i in range(board_len):
        row = []
        for j in range(board_len):
            if (i == 0 or i == 7) and (j == 0 or j == 7):
                row.append("X")
            else:
                row.append("-")
        board.append(row)
    return board


def print_board(board):
    print("  01234567")
    i = 0
    for line in board:
        print(str(i) + " " + "".join(line))
        i += 1


# count the number of black and white pieces on a board configuration
def count(board):
    b = 0
    w = 0
    for row in board:
        for cell in row:
            if cell == "@":
                b += 1
            elif cell == "O":
                w += 1
    return b, w


#count the number of friends, enemies, edges and corners surrounding a given 
#piece on a board configuration
def count_adjacent(board, colour):
    if colour == "white":
        symbol = "O"
    else:
        symbol = "@"

    friends = 0
    enemies = 0
    edges = 0
    corners = 0

    w = len(board)
    for i in range(w):
        for j in range(w):
            if board[i][j] == symbol:
                b, w, e, c = count_adjacent_cell(board, i, j)
                edges += e
                corners += c
                if symbol == "@":
                    friends += b
                    enemies += w
                else:
                    friends += w
                    enemies += b
    return friends, enemies, edges, corners


def count_adjacent_cell(board, i, j):
    ## NOT FUCKEN WORKING
    b,w,e,c = 0,0,0,0
    # check row above
    if i > 0:
        # not in top row
        for x in [j-1, j, j+1]:
            if(x >= 0 and x < len(board)):
                neighbour = board[i-1][j]
                if neighbour == "@":
                    b += 1
                elif neighbour == "O":
                    w += 1
                elif neighbour == "X":
                    c += 1
                elif neighbour == "#":
                    e += 1
    else:
        e += 1

    # check row below
    if i < len(board)-1:
        # not in bottom row
        for x in [j-1, j, j+1]:
            if(x >= 0 and x < len(board)):
                neighbour = board[i+1][j]
                if neighbour == "@":
                    b += 1
                elif neighbour == "O":
                    w += 1
                elif neighbour == "X":
                    c += 1
                elif neighbour == "#":
                    e += 1
    else:
        e += 1

    # check left and right
    if j > 0:
        neighbour = board[i][j-1]
        if neighbour == "@":
            b += 1
        elif neighbour == "O":
            w += 1
        elif neighbour == "X":
            c += 1
        elif neighbour == "#":
            e += 1
    else:
        e += 1

    if j < len(board)-1:
        neighbour = board[i][j+1]
        if neighbour == "@":
            b += 1
        elif neighbour == "O":
            w += 1
        elif neighbour == "X":
            c += 1
        elif neighbour == "#":
            e += 1
    else:
        e += 1
    return b,w,e,c

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
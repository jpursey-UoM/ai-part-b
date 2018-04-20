from state import *
from Move import *

def convert_board(board_list):
    # convert the input list of strings to a list of lists of chars,
    # without spaces
    new_list = [None] * len(board_list)
    for i in range(len(board_list)):
        # strip spaces
        board_list[i] = board_list[i].replace(" ", "")
        board_list[i] = board_list[i].strip("\n")
        # copy row to new_list
        new_list[i] = list(board_list[i])  # dirty

    return new_list

# make a new (empty) board array
def new_board():
    board_len = 8
    board = []
    for i in range(board_len):
        row = []
        for j in range(board_len):
            if(i == 0 or i == 7) and (j==0 or j == 7):
                row.append("X")
            else:
                row.append("-")
        board.append(row)
    return board


board = new_board()
board[1][1] = "@"
board[1][2] = "@"
board[1][3] = "O"
board[3][3] = "O"

board[4][1] = "@"
board[5][1] = "O"  # should be surrounded by corner

board[6][4] = "@"
board[6][5] = "O"  # should be surrounded by corner

board[1][4] = "@"
board[1][5] = "O"  # should be surrounded by corner

board[2][6] = "@"
board[3][6] = "O"  # should be surrounded by corner


current = State(127+24, -1, board)
current.print_board()

next_state = State.generate(current, Move(3,3,4,3));
next_state.print_board()

next_state.board[2][3] = "O"
next_state.print_board()
next_state = State.generate(next_state, Move(3,2,3,1))
next_state.print_board()

next_state.turns = 191 + 24
another_state = State.generate(next_state, Move(4,6,4,5))
another_state.print_board()


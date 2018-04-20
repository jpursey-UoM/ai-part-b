from state import *
from turn import *


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
            if(i == 0 or i == 7) and (j == 0 or j == 7):
                row.append("X")
            else:
                row.append("-")
        board.append(row)
    return board


board = new_board()
first = State(0, -1, board)
place_turn = Turn("place",  (3, 3), "white")
second = State.generate(first, place_turn)
second.print_board()
place_turn2 = Turn("place",  (1, 1), "black")
third = State.generate(second, place_turn2)
third.print_board()
move_turn = Turn("move", ((3, 3), (2, 3)), "white")
fourth = State.generate(third, move_turn)
fourth.print_board()



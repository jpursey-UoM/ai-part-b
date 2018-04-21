import random

from game.MoveFinder import *
from game.state import *


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
current = State(0, -1, board)
mf = MoveFinder()
player = "white"
i = 0
while (True):
    print("i: " + str(i))
    turns = mf.find_all_turns(player, current)
    if len(turns) == 0:
        print(player + " loses!")
        break
    turn = random.choice(turns)
    print(turn)
    current = State.generate(current, turn)
    current.print_board()
    print()
    if player == "white":
        player = "black"
    else:
        player = "white"
    i += 1



import itertools
import sys
from graph.node import *
from game.MoveFinder import *
from graph.greedysearch import *
from game.turn import *

MASSACRE_S = "Massacre"
MOVES_S = "Moves"

CUT_OFF_DEPTH = 1000  # max depth to consider. prints nothing if not possible

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


# read input from stdin
input_lines = list(itertools.islice(sys.stdin, 9))


instruction = input_lines[-1].strip("\n")
initial_state = State(0, "white", convert_board(input_lines[:8]))

root = Node(initial_state, None, None)


if instruction == MASSACRE_S:
    goal = greedy_bf_search(root, CUT_OFF_DEPTH)
    if(goal is not None):
        moves = goal.get_path()
        for m in moves:
            assert(type(m) == Turn)
            print(m.to_string())
elif instruction == MOVES_S:
    mf = MoveFinder()
    # print white
    print(len(mf.find_all_turns("O", root.board)))
    # print black
    print(len(mf.find_all_turns("@", root.board)))

from MoveFinder import *
from state import *

# COMP30024 Part B
# Player that picks randomly from the possible moves
# Author: Jason Pursey 637551


class Player:
    current = None
    colour = None
    def __init__(self, colour):
        self.current = State(0, -1, self.new_board())

    def action(self, turns):
        print("to do: implement Player.action(turns)")

    def update(self, action):
        print("to do: implement Player.update(action)")

    # make a new (empty) board array
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

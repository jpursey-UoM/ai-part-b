from MoveFinder import *
from state import *
import random

# COMP30024 Part B
# Player that picks randomly from the possible moves
# Author: Jason Pursey 637551


class Player:

    def __init__(self, colour):
        self.current = State(0, -1, Player.new_board())
        self.colour = colour
        self.mf = MoveFinder()

    def action(self, turns):
        # get all the possible actions
        possible = self.mf.find_all_turns(self.colour, self.current)
        # choose one randomly
        choice = random.choice(possible)
        # update our model
        self.update(choice.action, self.colour)

        return choice.action

    def update(self, action, colour=None):
        if colour is None:
            if self.colour == "black":
                colour = "white"
            else:
                colour = "black"

        turn_type = ""
        if action is not None:
            if type(action[0]) == int:
                turn_type = "place"
            else:
                turn_type = "move"
        else:
            turn_type = "pass"

        turn = Turn(turn_type, action, colour)
        self.current = State.generate(self.current, turn)

    # make a new (empty) board array
    @staticmethod
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

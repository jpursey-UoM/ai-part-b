from game.MoveFinder import *
from game.state import *
import game.board as board
import random

# COMP30024 Part B
# Player that picks randomly from the possible moves
# Author: Jason Pursey 637551


class Player:

    def __init__(self, colour):
        self.current = State(0, -1, board.new_board())
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



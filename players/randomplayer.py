from game.MoveFinder import *
from game.state import *
import game.board as board
import random
from game.watchyourback import *

# COMP30024 Part B
# Player that picks randomly from the possible moves
# Author: Jason Pursey 637551


class Player:

    def __init__(self, colour):
        self.colour = colour
        self.game = WatchYourBack()
        self.state = self.game.initial

    def action(self, turns):
        # get all the possible actions
        possible = self.state.moves
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
        if colour == "white":
            symbol = "O"
        else:
            symbol = "@"

        turn_type = ""
        if action is not None:
            if type(action[0]) == int:
                turn_type = "place"
            else:
                turn_type = "move"
        else:
            turn_type = "pass"

        turn = Turn(turn_type, action, symbol)
        self.state = self.game.result(self.state, turn)



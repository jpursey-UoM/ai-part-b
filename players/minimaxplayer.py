from game.state import *
from game.MoveFinder import *
import game.board as board
import graph.minimax as minimax

# COMP30024 Part B
# Just the required methods for players
# Author: Jason Pursey 637551


class Player:

    def __init__(self, colour):
        self.current = State(0, -1, board.new_board())
        self.colour = colour
        self.mf = MoveFinder()

    def action(self, turns):
        turn = minimax.find_best(self.current, self.colour)
        self.update(turn.action, self.colour)
        return turn.action

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

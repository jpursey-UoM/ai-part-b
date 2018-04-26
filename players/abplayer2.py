
from game.watchyourback import *

# COMP30024 Part B
# Player that uses minimax with alpha beta pruning
# Author: Jason Pursey 637551


class Player:

    def __init__(self, colour):
        self.colour = colour
        self.game = WatchYourBack()
        self.state = self.game.initial

    def action(self, turns):
        # use AIMA alphabeta alg
        choice = alphabeta_cutoff_search(self.state, self.game, 1, None, self.eval)
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


    def eval(self, state):
        # greedy and dumb eval function
        board = state.board
        b,w = boardutils.count(board)
        diff = b - w
        if self.colour == "white":
            return -diff
        else:
            return diff

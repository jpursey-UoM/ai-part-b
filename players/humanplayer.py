from game.MoveFinder import *
from game.state import *
import game.boardutils as board
import random
from game.watchyourback import *

# COMP30024 Part B
# Player that asks for moves from human user
# Author: Jason Pursey 637551


class Player:

    def __init__(self, colour):
        self.colour = colour
        self.game = WatchYourBack()
        self.state = self.game.initial

    def action(self, turns):
        # get all the possible actions
        possible = self.state.moves
        # ask for input
        have_input = False
        choice=None
        while (not have_input):
            response = input(">")
            if response == "h":
                # print help
                print("Enter desired turn of the form 'x y' for placing " +
                      "or 'x1 y1 x2 y2' for moving.")
                print("Specials:")
                print("m -  list all possible moves")
                print("r -  choose randomly")
                print("q -  quit")
                print("h -  show this help")
                continue
            elif response == "m":
                for move in self.state.moves:
                    print(move)
                continue
            elif response == "r":
                choice = random.choice(self.state.moves)
                have_input = True
            elif response == "q":
                quit(0)
            else:
                parts = response.split(" ")
                if self.colour == "white":
                    symbol = "O"
                else:
                    symbol = "@"

                if len(parts) == 2:
                    choice = Turn("place", (int(parts[0]), int(parts[1])), symbol)
                    print(choice)
                elif len(parts) == 4:
                    choice = Turn("move", ((int(parts[0]), int(parts[1])),
                                           (int(parts[2]), int(parts[3]))), symbol)
                if choice not in self.state.moves:
                    print("Invalid move! Enter m to list possible moves")
                else:
                    have_input = True



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



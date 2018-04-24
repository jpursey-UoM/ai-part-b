import game.state as state
from game.game import *
from game.MoveFinder import *
from game.board import *

class WatchYourBack(Game):

    def __init__(self):
        board = new_board()
        self.mf = MoveFinder()
        moves = self.mf.find_all_turns("O",board, 0)
        # add turns_taken to gamestate?
        self.initial = GameState(to_move="O", utility=0,
                                 board=board,
                                 moves=moves, turns_taken=0)

    def actions(self, state):
        return state.moves

    def result(self, gamestate, move):
        board = state.generate(gamestate, move)
        turns_taken = gamestate.turns_taken + 1
        if gamestate.to_move == "@":
            to_move = "O"
        else:
            to_move = "@"

        moves = self.mf.find_all_turns(to_move, board, turns_taken)
        utility = WatchYourBack.compute_utility(board, turns_taken)
        return GameState(to_move=to_move, utility=utility, board=board,
                         moves=moves, turns_taken=turns_taken)

    def utility(self, state, player):
        if player == "O":
            return state.utility
        else:
            return -state.utility

    def terminal_test(self, state):
        if state.utility != 0 or len(state.moves) == 0:
            return True
        else:
            return False

    def display(self, state):
        print("Total turns: " + str(state.turns_taken))
        print(state.to_move + "'s turn")
        print_board(state.board)

    @staticmethod
    def compute_utility(board, turns_taken):
        """ If winning state for white, return 1, for black return -1
        else return 0"""
        if turns_taken < 24:
            # can't win in placing phase
            return 0
        b, w = WatchYourBack.count(board)
        if b < 2:
            return 1
        elif w < 2:
            return -1
        else:
            return 0

    @staticmethod
    def count(board):
        b = 0
        w = 0
        for row in board:
            for cell in row:
                if cell == "@":
                    b += 1
                elif cell == "O":
                    w += 1
        return b, w
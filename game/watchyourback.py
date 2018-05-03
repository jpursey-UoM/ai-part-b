import game.state as state
from game.game import *
from game.MoveFinder import *
import game.boardutils as boardutils

class WatchYourBack(Game):

    def __init__(self):
        """we create an object of the inherited class "Game" to 
        initialize the game"""
        board = boardutils.new_board()
        self.mf = MoveFinder()
        moves = self.mf.find_all_turns("O",board, 0)
        # add turns_taken to gamestate?
        self.initial = GameState(to_move="O", utility=0,
                                 board=board,
                                 moves=moves, turns_taken=0)

    def actions(self, state):
        """given a game state, this method generates all the legal 
        actions possible from this state, as a list"""
        return state.moves

    def result(self, gamestate, move):
        """given a game state and a move, this method returns the 
        game state that we get by making that move on this state"""
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
        """given a terminal game state and a player, this method returns 
        the utility for that player in the given terminal game state"""
        if player == "O":
            return state.utility
        else:
            return -state.utility

    def terminal_test(self, state):
        """given a game state, this method should return True if this 
        game state is a terminal state, and False otherwise"""
        if state.utility != 0 or len(state.moves) == 0:
            return True
        else:
            return False

    def display(self, state):
        """This method prints the current state of the game."""
        print("Total turns: " + str(state.turns_taken))
        print(state.to_move + "'s turn")
        boardutils.print_board(state.board)

    @staticmethod
    def compute_utility(board, turns_taken):
        """ Given a board configuration and the related number of turns 
        taken, this methods calculates the utility of Watchyourback game. 
        If winning state for white, return 1, for black return -1 and
        else return 0"""
        if turns_taken < 24:
            # can't win in placing phase
            return 0
        b, w = boardutils.count(board)
        if b == w:
            return 0
        elif b < 2:
            return 1
        elif w < 2:
            return -1
        else:
            return 0

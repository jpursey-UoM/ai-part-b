from game.MoveFinder import *
from game.state import *

class Node:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.mm_score = None
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

    def add_child(self, child):
        assert (type(child) == Node)
        self.children += [child]

    def expand(self):
        # find all possible moves
        mf = MoveFinder()

        if self.state.current_player == -1:
            symbol = "0"
        else:
            symbol = "@"

        turns = mf.find_all_turns(symbol, self.state)
        # generate new boards and nodes for each move
        for turn in turns:

            s = State.generate(self.state, turn)
            child = Node(s, self)
            self.add_child(child)
        return self.children

    def get_path(self):
        path = []
        current_node = self
        while current_node.move is not None:
            path.append(current_node.move)
            current_node = current_node.parent

        return path[::-1]

    def set_minimax_val(self, val):
        self.mm_score = val

    def get_minimax_val(self):
        return self.mm_score

    def get_children(self):
        return self.children

    def __eq__(self, other):
        return self.board.black == other.board.black

    def __gt__(self, other):
        return self.board.black > other.board.black

    def __lt__(self, other):
        return self.board.black < other.board.black
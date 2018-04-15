from MoveFinder import *
from Board import *

class Node:
    parent = None
    children = []
    board = None
    move = None
    depth = None

    def __init__(self, board, parent, move):
        self.board = board
        self.parent = parent
        self.move = move
        if(parent is None):
            self.depth = 0
        else:
            self.depth = parent.depth + 1

    def add_child(self, child):
        assert (type(child) == Node)
        self.children += [child]

    def expand(self):
        # find all possible moves
        mf = MoveFinder()
        moves = mf.find_all_moves("O", self.board)
        # generate new boards and nodes for each move
        children = []   # list of nodes
        for move in moves:
            b = Board.generate(self.board, move)
            child = Node(b, self, move)
            children.append(child)

        return children

    def get_path(self):
        path = []
        current_node = self
        while (current_node.move is not None):
            path.append(current_node.move)
            current_node = current_node.parent

        return path[::-1]

    def __eq__(self, other):
        return self.board.black == other.board.black

    def __gt__(self, other):
        return self.board.black > other.board.black

    def __lt__(self, other):
        return self.board.black < other.board.black
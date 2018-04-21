from game.turn import Turn
from queue import Queue
import graph.node as node


def find_best(current, player):
    root = node.Node(current)
    depth = current.turns

    if player == "white":
        nextplayer = "black"
    elif player == "black":
        nextplayer = "white"

    best_score = -100000
    best_child = None
    for child in root.expand():
        s = minimax_value(child, nextplayer, depth)
        if s > best_score:
            best_child = child
            best_score = s

    return best_child.state.turn


def minimax_value(node, player, depth):
    maxturn = (player == "white" and node.state.current_player == 1)

    if is_terminal(node.state, depth):
        return utility(node.state)
    elif maxturn:
        return max([minimax_value(c, player, depth) for c in node.expand()])
    else:
        return min([minimax_value(c, player, depth) for c in node.expand()])


def utility(state):
    b,w = count(state.board)
    f = state.current_player # -1 for white, 1 for black

    if w < 2:
        if b >= 2:
            # winning state for black
            return 1*f
        else:
            # draw state, both < 2
            return 0
    elif b < 2:
        # winning state for white
        return -1*f
    else:
        # both > 2, no bonus
        return 0


def count(board):
    b = 0
    w = 0
    for row in board:
        for cell in row:
            if cell == "@":
                b += 1
            elif cell == "O":
                w += 1
    return b,w


def is_terminal(state, depth):
    if state.turns < 24:
        return False
    if state.turns - depth > 3:
        # only look 3 turns ahead
        return True
    b,w = count(state.board)
    return (b < 2 or w < 2)


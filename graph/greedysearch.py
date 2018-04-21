
from queue import PriorityQueue

# Functions that allow a greedy best-first search of a tree, looking for a
# state with no black pieces left
# Entry point is greedy_bf_search(root)
# root should be of type Node, containing the initial board state

# returns a node containing a goal state
def greedy_bf_search(root, depth_limit):
    q = PriorityQueue()
    q.put((p(root), root))
    while not q.empty():
        # pop the best found so far
        priority, node = q.get()
        if(node.depth > depth_limit):
            continue    # this node too deep, but others in queue may still be ok

        if is_goal(node):
            return node

        children = node.expand()
        for child in children:
            pair = (p(child), child)
            q.put(pair)

# priority (lower is better)
def p(node):
    diff = node.board.black - node.board.white
    return diff


# true if all black pieces gone, at least one white piece left
def is_goal(node):
    if node.board.black == 0 and node.board.white >= 1:
        return True
    else:
        return False

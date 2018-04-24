from game.watchyourback import *

game = WatchYourBack()
state = game.initial
moves = state.moves
random.shuffle(moves)
for move in moves:
    print(move)


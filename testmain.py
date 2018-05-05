from game.watchyourback import *

game = WatchYourBack()
state = game.initial
moves = state.moves
random.shuffle(moves)
turn = random.choice(moves)
state = game.result(state, Turn("place", turn, "@"))


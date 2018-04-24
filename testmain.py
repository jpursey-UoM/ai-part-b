from game.watchyourback import *

game = WatchYourBack()
state = game.initial
for i in range(220):
    move = random.choice(state.moves)
    print(move)
    state = game.result(state, move)
    game.display(state)


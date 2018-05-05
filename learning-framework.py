import trainingref as ref

import players.tdplayer
import players.abplayer2
from random import randint
#

def play_game(learner):
    coin = randint(0, 1)
    if coin:
        learner.reset("white")
        p1 = learner
        p2 = players.abplayer2.Player("black")
    else:
        learner.reset("black")
        p2 = learner
        p1 = players.abplayer2.Player("white")
    print("learner is " + learner.colour)
    winner = ref.main(p1, p2)
    print("winner: " + winner)

    if ((winner == "W" and p1 == learner) or
        (winner == "B" and p2 == learner)):
        return 1
    else:
        return -1


learner = players.tdplayer.Player("white")
for i in range(10):
    print(f"Game {i+1}")
    result = play_game(learner)
    learner.teach(result)
    print(f"result: {result}")

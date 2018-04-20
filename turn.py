class Turn:
    action = None
    type = None
    player = None

    def __init__(self, turn_type, action, player):
        assert((turn_type == "place") or (turn_type == "move"))
        self.type = turn_type
        self.action = action
        self.player = player

    def get_action(self):
        return self.action

    def get_action_parts(self):
        a = self.action
        if self.type == "move":
            return [a[0][0], a[0][1], a[1][0], a[1][1]]
        elif self.type == "place":
            return [a[0], a[1]]

    def to_string(self):
        return "("+str(self.action[0]) + " -> " + str(self.action[1]) + ")"

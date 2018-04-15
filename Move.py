class Move:
    start_x=None
    start_y=None
    end_x=None
    end_y=None

    def __init__(self, x1, y1, x2, y2):
        self.start_x=x1
        self.start_y=y1
        self.end_x=x2
        self.end_y=y2

    def getMove(self):
        return [self.start_x,self.start_y,self.end_x,self.end_y]

    def toString(self):
        return("("+str(self.start_x)+" ,"+str(self.start_y)+") -> ("+
               str(self.end_x)+", "+str(self.end_y)) + ")"

class State:
    board = []
    # 2d array of chars representing board and pieces.
    # blank: "-",  black: "@", white: "O"
    turns = None  # int. total number of moves made by BOTH players so far
    current_player = None  # int.  -1 = "white" or  1 = "black"



    # generate state based on provided board
    def __init__(self, turns, current_player,  board_list):
        self.turns = turns
        self.current_player = current_player
        self.board = board_list

    @staticmethod
    def is_surrounded(x, y, board_array):
        if(x<0 or y<0 or x>=len(board_array) or y>=len(board_array)) :
            return False
        centre = board_array[y][x]
        bad = ["X"]
        if (centre == "O"):
            bad.append("@")
        elif (centre == "@"):
            bad.append("O")

        # up and down
        if (y > 0 and y < len(board_array) - 1):
            up = board_array[y - 1][x]
            down = board_array[y + 1][x]
            if (up in bad) and (down in bad):
                return True

        # left and right
        if (x > 0 and x < len(board_array[0]) - 1):
            left = board_array[y][x - 1]
            right = board_array[y][x + 1]
            if (left in bad) and (right in bad):
                return True

        return False
    # generate board based on parent and move
    @staticmethod
    def generate(parent_b, move_m):
        # copy parent

        array = []
        for row in parent_b.array:
            array.append(list(row))

        # move one piece based on move
        x1 = move_m.start_x
        y1 = move_m.start_y
        x2 = move_m.end_x
        y2 = move_m.end_y

        temp = array[y1][x1]
        array[y1][x1] = array[y2][x2]
        array[y2][x2] = temp

        # work out which (if any) pieces got taken
        if(State.is_surrounded(x2 - 1, y2, array)) :
            array[y2][x2-1]="-"
        if (State.is_surrounded(x2 + 1, y2, array)):
            array[y2][x2 + 1] = "-"
        if (State.is_surrounded(x2, y2 - 1, array)) :
            array[y2-1][x2]="-"
        if (State.is_surrounded(x2, y2 + 1, array)):
            array[y2+1][x2] = "-"
        if(State.is_surrounded(x2, y2, array)) :
            array[y2][x2]="-"
        # create and return the Board object

        return State(array)

    def print_board(self):
        print("  01234567")
        i = 0
        for line in self.board:
            print(str(i) + " " + "".join(line))
            i += 1


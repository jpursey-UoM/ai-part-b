class State:
    # board: 2d array of chars representing board and pieces.
    #       blank: "-",  black: "@", white: "O", removed by dz: "#"
    # turns: int. total number of turns made by BOTH players so far
    # current_player: int.  -1 = "white" or  1 = "black"



    # generate state based on provided board
    def __init__(self, turns, current_player,  board_list, turn=None):
        self.turns = turns
        self.current_player = current_player
        self.board = board_list
        self.turn = turn  # turn that generated this state

    @staticmethod
    def is_surrounded(row, col, board_array):
        x = col
        y = row
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
    def generate(previous, turn):
        # copy parent

        board = []
        for row in previous.board:
            board.append(list(row))
        if turn.type != "pass":
            if turn.type == "move":
                # move one piece based on move
                x1, y1, x2, y2 = turn.get_action_parts()

                temp = board[y1][x1]
                board[y1][x1] = board[y2][x2]
                board[y2][x2] = temp
            elif turn.type == "place":
                x2, y2 = turn.get_action_parts()
                if turn.player == "white":
                    board[y2][x2] = "O"
                elif turn.player == "black":
                    board[y2][x2] = "@"

            # work out which (if any) pieces got taken
            if(State.is_surrounded(y2, x2 - 1, board)) :
                State.clear_square(y2, x2 - 1, board)
            if (State.is_surrounded(y2, x2 + 1, board)):
                State.clear_square(y2, x2 + 1, board)
            if (State.is_surrounded(y2 - 1, x2, board)) :
                State.clear_square(y2 - 1, x2, board)
            if (State.is_surrounded(y2 + 1, x2, board)):
                State.clear_square(y2 + 1, x2, board)
            if(State.is_surrounded(y2, x2, board)) :
                State.clear_square(y2, x2, board)

        # check if board needs to shrink
        turns = previous.turns + 1
        if turns == 128 + 24:  # 24 is number of turns in placing phase
            board = State.shrink_board(board, 128)
        if turns == 192 + 24:
            board = State.shrink_board(board, 192)

        # create and return the State object
        return State(turns, -1*previous.current_player, board, turn)

    def print_board(self):
        print("  01234567")
        i = 0
        for line in self.board:
            print(str(i) + " " + "".join(line))
            i += 1

    @staticmethod
    def shrink_board(board, dz_type):
        width = 0  # width of dead space padding
        if dz_type == 128:
            width = 1
        if dz_type == 192:
            width = 2

        # update edges
        for i in range(width - 1, len(board) - (width - 1)):
            board[width - 1][i] = "#"
            board[i][width - 1] = "#"
            board[-width][i] = "#"
            board[i][-width] = "#"

        # update corners
        board[width][width] = "X"
        board[width][-(width + 1)] = "X"
        board[- (width + 1)][width] = "X"
        board[- (width + 1)][- (width + 1)] = "X"

        # check if remaining pieces surrounded (outer edges of remaining space)
        start = width
        end = len(board) - width
        iterator = range(start, end)

        # down col 1
        for i in iterator:
            if State.is_surrounded(i, start, board):
                State.clear_square(i, start, board)

        # right along row 6
        for i in iterator:
            if State.is_surrounded(end - 1, i, board):
                State.clear_square(end - 1, i, board)

        # up col 6
        for i in reversed(iterator):
            if State.is_surrounded(i, end - 1, board):
                State.clear_square(i, end - 1, board)

        # left along row 1
        for i in reversed(iterator):
            if State.is_surrounded(start, i, board):
                State.clear_square(start, i, board)

        return board

    @staticmethod
    def clear_square(row, col, board):
        board[row][col] = "-"

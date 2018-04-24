from game.turn import *


class MoveFinder:
    BOARD_SIZE = 7  # max index of rows, cols
    CORNER = "X"
    PIECES = ["@", "O"]  # characters that represent pieces

    def check_valid(self, board, row, col):
        # within the boundaries
        if ((row < 0) or (row > self.BOARD_SIZE) or (col < 0) or
                (col > self.BOARD_SIZE)):
            return False
        # not occupied and not a corner
        if board[row][col] != "-":
            return False

        return True

    # find all possible actions for all pieces of player's colour
    def find_all_turns(self, player, board, turns_taken):
        turns = []

        # check if in placing phase or moving phase
        if turns_taken < 24:
            turns = self.find_places(player, board)
        else:
            symbol = player
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == symbol:
                        turns += (self.find_moves(row, col, board, player))

        if len(turns) == 0:
            turns.append(Turn("pass", None, player))  # forfeited turn
        return turns

    def find_places(self, player, board):
        start_row = 0
        end_row = 7
        if player == "@":
            start_row = 2
        elif player == "O":
            end_row = 5

        turns = []
        for row in range(start_row, end_row + 1):
            for col in range(8):
                if self.check_valid(board, row, col):
                    turns.append(Turn("place", (col, row), player))

        return turns

    # find all moves for a particular piece
    def find_moves(self, row, col, board, player):
        # check there's a piece
        if not board[row][col] in self.PIECES:
            return None

        moves = []

        # check up
        if(self.check_valid(board, row - 1, col)):
            moves.append(Turn("move", ((col, row), (col, row - 1)), player))
        elif(self.check_valid(board, row - 2, col)):
            moves.append(Turn("move", ((col, row), (col, row - 2)), player))

        # check down
        if(self.check_valid(board, row + 1, col)):
            moves.append(Turn("move", ((col, row), (col, row + 1)), player))
        elif(self.check_valid(board, row + 2, col)):
            moves.append(Turn("move", ((col, row), (col, row + 2)), player))

        # check left
        if (self.check_valid(board, row, col - 1)):
            moves.append(Turn("move", ((col, row), (col - 1, row)), player))
        elif (self.check_valid(board, row, col - 2)):
            moves.append(Turn("move", ((col, row), (col - 2, row)), player))

        # check right
        if (self.check_valid(board, row, col + 1)):
            moves.append(Turn("move", ((col, row), (col + 1, row)), player))
        elif (self.check_valid(board, row, col + 2)):
            moves.append(Turn("move", ((col, row), (col + 2, row)), player))

        return moves

    def count_moves(self, row, col, board):
        return len(self.find_moves(row, col, board))

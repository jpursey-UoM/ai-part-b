from Move import *


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
        if (board.array[row][col] != "-"):
            return False

        return True

    def find_all_moves(self, symbol, board):
        board_array = board.array
        moves = []
        for row in range(len(board_array)):
            for cell in range(len(board_array[row])):
                if board_array[row][cell] == symbol:
                  moves += (self.find_moves(row, cell, board))
        return moves

    def find_moves(self, row, col, board):
        board_l = board.array
        # check there's a piece
        if not board_l[row][col] in self.PIECES:
            return None

        moves = []

        # check up
        if(self.check_valid(board, row - 1, col)):
            moves += [Move(col, row, col, row - 1)]
        elif(self.check_valid(board, row - 2, col)):
            moves += [Move(col, row, col, row - 2)]

        # check down
        if(self.check_valid(board, row + 1, col)):
            moves += [Move(col, row, col, row + 1)]
        elif(self.check_valid(board, row + 2, col)):
            moves += [Move(col, row, col, row + 2)]

        # check left
        if (self.check_valid(board, row, col - 1)):
            moves += [Move(col, row, col -1 , row)]
        elif (self.check_valid(board, row, col - 2)):
            moves += [Move(col, row, col - 2, row)]

        # check right
        if (self.check_valid(board, row, col + 1)):
            moves += [Move(col, row, col + 1, row)]
        elif (self.check_valid(board, row, col + 2)):
            moves += [Move(col, row, col + 2, row)]

        return moves

    def count_moves(self, row, col, board):
        return len(self.find_moves(row, col, board))

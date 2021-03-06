# !/usr/bin/python
# -*- coding: utf-8 -*-


class Board:
    """
    Helper class to represent both a TicTacBoard and the main board
    """
    def __init__(self):
        self.board = [None]*9
        self.is_full = False
        self.has_winner = False
        self.winner = None

    def check_function_winner(self, func, winner):
        """
        Checks for a winner.
        'func' should be a function implemented by TicTacBoard and GameBoard
        """
        row_count = col_count = diag1_count = diag2_count = 0

        for i in range(3):
            if func(self.board[i*4]):    # checks main diagonal
                diag1_count += 1
            if func(self.board[i*2 + 2]):    # checks secondary diagonal
                diag2_count += 1
            for j in range(3):
                if func(self.board[i*3 + j]):    # checks rows
                    row_count += 1
                if func(self.board[j + 3 * i]):  # checks cols
                    col_count += 1

        if max((row_count, col_count, diag1_count, diag2_count)) >= 3:
            self.has_winner = True
            self.winner = winner
            return True

        return False

    @staticmethod
    def valid_pos(pos):
        """
        Checks if a given posisition is numericly valid
        """
        if pos < 0 or pos > 8:
            raise IndexError("Position out of bounds for board.\n\n")

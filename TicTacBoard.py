# !/usr/bin/python
# -*- coding: utf-8 -*-

from Board import Board


class TicTacBoard(Board):
    """
    Represents a single TicTac board.
    """
    def __init__(self):
        super(TicTacBoard, self).__init__()
        for idx, _ in enumerate(self.board):
            self.board[idx] = " "

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x == piece, piece)

    def move(self, piece, pos):
        super().valid_pos(pos)
        if self.board[pos] is not None:
            raise ValueError("Position already taken!")
        self.board[pos] = piece
        self.check_winner(piece)

    def print_line(self, line, last=False):
        """
        Prints a single a line of the board. Lines are 0 indexed (0, 1 or 2)
        """
        string_line = ""
        print(*self.board[line*3:line*3 + 3], sep="|", end="")
        if not last:
            print("  |  ", end="")

    def test(self):
        # TODO: Remove before going into production
        for i in [0, 3, 4, 8]:
            self.board[i] = "X"
        for i in [1, 2, 6]:
            self.board[i] = "O"


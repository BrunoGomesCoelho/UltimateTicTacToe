# !/usr/bin/python
# -*- coding: utf-8 -*-

from Board import Board


class TicTacBoard(Board):
    """
    Represents a single TicTac board.
    """
    def __init__(self):
        super(TicTacBoard, self).__init__()
        for i in range(9):
            self.board[i] = i

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x == piece, piece)

    def move(self, piece, pos):
        super().valid_pos(pos)
        if self.board[pos] is not None:
            raise ValueError("Position already taken!")
        self.board[pos] = piece
        self.check_winner(piece)

    def __str__(self):
        for row in range(3):
            print(" ", end="")
            print(*self.board[row*3:row*3+3], sep=" | ")
        return ""

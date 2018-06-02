# !/usr/bin/python
# -*- coding: utf-8 -*-
from Board import Board


class TicTacBoard(Board):
    """
    Represents a single TicTac board.
    """
    def __init__(self):
        super(TicTacBoard, self).__init__()

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x == piece, piece)

    def move(self, piece, pos):
        super().valid_pos(pos)
        if self.board[pos] is not None:
            raise ValueError("Position already taken!")
        self.board[pos] = piece
        self.check_winner(piece)

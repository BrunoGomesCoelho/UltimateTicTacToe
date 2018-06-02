# !/usr/bin/python
# -*- coding: utf-8 -*-
from Board import Board


class GameBoard(Board):
    def __init__(self):
        super().__init__()

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x is not None and x.winner == piece, piece)

    def add_move(self, piece, tic_tac_board, pos):
        pass

    def __str__(self):
        pass

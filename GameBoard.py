# !/usr/bin/python
# -*- coding: utf-8 -*-
from Board import Board


class GameBoard(Board):
	def __init__(self):
		super(GameBoard, self).__init__()

	def win_function(self, piece):
		return super().check_win(lambda x: x is not None and x.winner == piece, piece)

	def add_move(self, piece, tic_tac_board, pos):
		pass

	def check_winner(self):
		pass

	def __str__(self):
		pass

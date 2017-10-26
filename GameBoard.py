# !/usr/bin/python
# -*- coding: utf-8 -*-
from TicTacBoard import TicTacBoard


class GameBoard:
	def __init__(self):
		self.is_full = None
		self.has_winner = None
		self.winner = None
		self.game_board = [TicTacBoard() for _ in range(9)]

	def get_winner(self):
		pass

	def add_move(self, piece, tic_tac_board, pos):
		pass

	def __str__(self):
		pass

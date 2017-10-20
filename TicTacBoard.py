# !/usr/bin/python
# -*- coding: utf-8 -*-


class TicTacBoard:
	def __init__(self):
		self.board = []*9
		self.is_full = None
		self.has_winner = None
		self.winner = None

	def move(self, piece, num):
		if self.board[num] is not None:
			raise Exception("Invalid position")
		else:
			self.board[num] = piece

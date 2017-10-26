# !/usr/bin/python
# -*- coding: utf-8 -*-
from Board import Board


class TicTacBoard(Board):
	def __init__(self):
		super(TicTacBoard, self).__init__()

	def check_winner(self, piece):
		return super().check_winner(lambda x: x == piece, piece)

	def valid_move(self, move):
		if move < 0 or move > 8:
			raise IndexError("Piece out of bounds")
		if self.board[move] is not None:
			raise ValueError("Position already filled in")
		else:
			return True

	def move(self, piece, num):
		try:
			self.valid_move(num)
		except IndexError or ValueError:
			print(Exception)
		if self.valid_move(num):
			self.board[num] = piece
			self.check_win(num)



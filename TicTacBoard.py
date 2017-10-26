# !/usr/bin/python
# -*- coding: utf-8 -*-


class TicTacBoard:
	def __init__(self):
		self.board = [None]*9
		self.is_full = None
		self.has_winner = None
		self.winner = None

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

	def check_win(self, piece):
		row_count = col_count = diag1_count = diag2_count = 0

		for i in range(3):
			for j in range(3):
				if self.board[i*3 + j] == piece:    # checks rows
					row_count += 1
				if self.board[j + 3 * i] == piece:  # checks cols
					col_count += 1

		for i in range(3):
			if self.board[i*4] == piece:    # checks main diagonal
				diag1_count += 1
			if self.board[i*2 + 2] == piece:    # checks secondary diagonal
				diag2_count += 1

		if max((row_count, col_count, diag1_count, diag2_count)) >= 3:
			self.has_winner = True
			self.winner = piece
			return True
		else:
			return False

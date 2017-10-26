# !/usr/bin/python
# -*- coding: utf-8 -*-


class Board:
	def __init__(self):
		self.board = [None]*9
		self.is_full = None
		self.has_winner = None
		self.winner = None

	def check_winner(self, func, winner):
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
			else:
				return False

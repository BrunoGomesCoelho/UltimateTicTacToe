import pytest
from TicTacBoard import TicTacBoard


@pytest.fixture(scope='class')
def tbb():
	return TicTacBoard()


class TestTicTacBoard(object):

	def test_valid_move_out_of_bounds_positive(self):
		with pytest.raises(Exception):
			tbb.valid_move(9)

	def test_valid_move_out_of_bounds_negative(self):
		with pytest.raises(Exception):
			tbb.valid_move(-1)

	def test_valid_move_filled_o(self):
		with pytest.raises(Exception):
			a = tbb()
			a.board = ["X"] * 9
			a.valid_move(4)

	def test_valid_move_filled_x(self):
		with pytest.raises(Exception):
			a = tbb()
			a.board = ["O"] * 9
			a.valid_move(7)

	def test_check_win_row_win(self):
		piece = "X"
		a = tbb()
		a.board = [None, None, None, piece, piece, piece, None, None, None]
		assert a.check_winner(piece) and a.winner == piece and a.has_winner

	def test_check_win_col_win(self):
		piece = "O"
		a = tbb()
		a.board = [piece, None, None] + [piece, None, None] + [piece, None, None]
		assert a.check_winner(piece) and a.winner == piece and a.has_winner

	def test_check_win_main_diagonal(self):
		piece = "X"
		a = tbb()
		a.board = [piece, None, None] + [None, piece, None] + [None, None, piece]
		assert a.check_winner(piece) and a.winner == piece and a.has_winner

	def test_check_win_second_diagonal(self):
		piece = "O"
		a = tbb()
		a.board = [piece, None, None] + [None, piece, None] + [None, None, piece]
		assert a.check_winner(piece) and a.winner == piece and a.has_winner

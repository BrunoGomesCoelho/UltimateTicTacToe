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

	def test_check_winner_row_win(self):
		a = tbb()
		a.board = [None, None, None, "X", "X", "X", None, None, None]
		assert a.check_win("X") and a.winner == "X" and a.has_winner

	def test_check_winner_col_win(self):
		a = tbb()
		a.board = ["O", None, None] + ["O", None, None] + ["O", None, None]
		assert a.check_win("O") and a.winner == "O" and a.has_winner

	def test_check_winner_main_digonal(self):
		a = tbb()
		a.board = ["X", None, None] + [None, "X", None] + [None, None, "X"]
		assert a.check_win("X") and a.winner == "X" and a.has_winner

	def test_check_winner_second_diagonal(self):
		a = tbb()
		a.board = ["X", None, None] + [None, "X", None] + [None, None, "X"]
		assert a.check_win("X") and a.winner == "X" and a.has_winner

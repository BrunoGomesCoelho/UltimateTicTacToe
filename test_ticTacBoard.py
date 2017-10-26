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

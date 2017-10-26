import pytest
from GameBoard import GameBoard
from TicTacBoard import TicTacBoard


@pytest.fixture(scope="class")
def setup(board):
	a = GameBoard()
	element = TicTacBoard()
	element.has_winner = True
	element.winner = "X"
	a.board = [None if pos == None else element for pos in board]
	return a


class TestGameBoard(object):
	def test_check_win_row_win(self):
		a = setup([None, None, None, "tic tac board", "tic tac board", "tic tac board", None, None, None])
		assert a.check_winner("X") and a.winner == "X" and a.has_winner

	def test_check_win_col_win(self):
		a = setup(["tic tac board", None, None] + ["tic tac board", None, None] + ["tic tac board", None, None])
		assert a.check_winner("X") and a.winner == "X" and a.has_winner

	def test_check_win_main_diagonal(self):
		a = setup(["tic tac board", None, None] + [None, "tic tac board", None] + [None, None, "tic tac board"])
		assert a.check_winner("X") and a.winner == "X" and a.has_winner

	def test_check_win_second_diagonal(self):
		a = setup(["tic tac board", None, None] + [None, "tic tac board", None] + [None, None, "tic tac board"])
		assert a.check_winner("X") and a.winner == "X" and a.has_winner


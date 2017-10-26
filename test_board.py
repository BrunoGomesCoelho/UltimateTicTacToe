import pytest

from Board import Board


class TestBoard(object):

	def test_valid_pos_lower_0(self):
		with pytest.raises(Exception):
			b = Board()
			b.valid_pos(-1)

	def test_valid_pos_bigger_8(self):
		with pytest.raises(Exception):
			b = Board()
			b.valid_pos(9)

	def test_valid_pos_valid(self):
		b = Board()
		for i in range(9):
			b.valid_pos(i)

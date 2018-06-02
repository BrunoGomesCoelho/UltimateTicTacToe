# !/usr/bin/python
# -*- coding: utf-8 -*-

from Board import Board
import TicTacBoard


class GameBoard(Board):
    """
    Represents the main game board
    """
    def __init__(self):
        super().__init__()
        for idx, _ in enumerate(self.board):
            self.board[idx] = TicTacBoard.TicTacBoard()

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x is not None and x.winner == piece, piece)

    def add_move(self, piece, tic_tac_board, pos):
        pass

    def test(self):
        # TODO: Remove before going into production
        for tic_tac_board in self.board:
            tic_tac_board.test()

    def print(self):
        print("="*7 + " Game Board " + "="*7 + "\n\n")
        for _ in range(3):
            print("="*26)
            for line in range(3):
                for tic_tac_board in range(3):
                    if tic_tac_board == 2:
                        self.board[tic_tac_board].print_line(line, last=True)
                    else:
                        self.board[tic_tac_board].print_line(line, last=False)
                print()
        print("="*26 + "\n\n")

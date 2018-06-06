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
        self.winner = None
        self.is_full = False
        for idx, _ in enumerate(self.board):
            self.board[idx] = TicTacBoard.TicTacBoard()

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x is not None and x.winner == piece, piece)

    def move(self, piece, tic_tac_board, pos):
        self.valid_pos(tic_tac_board)
        has_winner, is_full = self.board[tic_tac_board].move(piece, pos)
        if has_winner:
            if self.check_winner(piece):
                self.winner = piece
                return True
        elif is_full:
            if self.check_full():
                self.is_full = True
        return False


    def check_full(self):
        is_full = True
        for cell in range(9):
            if not self.board[cell].is_full:
                is_full = False
                break
        return is_full



    def test(self):
        # TODO: Remove before going into production
        for tic_tac_board in self.board:
            tic_tac_board.test()

    def print(self):
        print("="*7 + " Game Board " + "="*7 + "\n\n")
        for row in range(3):
            print("="*26)
            for line in range(3):
                for tic_tac_board in range(row*3, row*3 +3):
                    if tic_tac_board == row*3+2:
                        self.board[tic_tac_board].print_line(line, last=True)
                    else:
                        self.board[tic_tac_board].print_line(line, last=False)
                print()
        print("="*26 + "\n\n")

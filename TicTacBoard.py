# !/usr/bin/python
# -*- coding: utf-8 -*-

from Board import Board

BLANK = "_"

class TicTacBoard(Board):
    """
    Represents a single TicTac board.
    """
    def __init__(self):
        self.game_over = False
        self.has_winner = False
        self.winner = None
        self.is_full = False
        super(TicTacBoard, self).__init__()
        for idx, _ in enumerate(self.board):
            self.board[idx] = BLANK

    def check_winner(self, piece):
        return super().check_function_winner(lambda x: x == piece, piece)


    def move(self, piece, pos):
        self.valid_pos(pos)
        if self.board[pos] is not BLANK:
            raise ValueError("Position already taken!\n\n")
        self.board[pos] = piece

        # Check for winner or full board
        if self.check_winner(piece):
            self.game_over = True
            self.has_winner = True
            self.winner = piece
        else:
            self.check_full()

        return self.has_winner, self.is_full

    def check_full(self):
        is_full = True
        for cell in range(9):
            if self.board[cell] is BLANK:
                is_full = False
                break
        self.game_over = is_full
        self.is_full = is_full
        return self.is_full


    def print_line(self, line, last=False):
        """
        Prints a single a line of the board. Lines are 0 indexed (0, 1 or 2)
        """
        print(*self.board[line*3:line*3 + 3], sep="|", end="")
        if not last:
            print("  |  ", end="")

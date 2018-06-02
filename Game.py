# !/usr/bin/python
# -*- coding: utf-8 -*-

import GameBoard
import Player

PLAYER_ONE = 0
PLANER_TWO = 1

MESSAGE_TURN = "Your turn player %d"

class Game:
    def __init__(self, player_one, player_two):
        self.next_turn = None
        self.is_running = True

        self.players = [Player.Player(*player_one), Player.Player(*player_two)]
        self.next_turn = PLAYER_ONE

    def __bool__(self):
        return self.is_running

    def next_move(self):
        print(MESSAGE_TURN % (self.next_turn + 1))
        self.is_running = False

    def print_results(self):
        pass


    def print(self):
        game_board = GameBoard.GameBoard()
        game_board.test()
        game_board.print()

        return ""

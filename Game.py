# !/usr/bin/python
# -*- coding: utf-8 -*-

import GameBoard
import Player

PLAYER_ONE = 0
PLAYER_TWO = 1

MESSAGE_TURN = "Your turn player %d"

class Game:
    def __init__(self, player_one, player_two):
        self.winner = None
        self.next_turn = PLAYER_ONE
        self.is_running = True

        self.players = [Player.Player(*player_one), Player.Player(*player_two)]
        self.game_board = GameBoard.GameBoard()


    def __bool__(self):
        return self.is_running


    def next_move(self):
        print(MESSAGE_TURN % (self.next_turn + 1))

        while True:
            tic_tac_board, pos = map(int, input("Please enter board and position: ").split())
            try:
                self.game_board.move(self.players[self.next_turn].piece, tic_tac_board, pos)
                print("Move added!\n\n")
                break
            except IndexError as error:
                print(error)
            except ValueError as error:
                print(error)

        if self.game_board.check_winner(self.players[self.next_turn].piece):
            self.winner = self.next_turn
            self.is_running = False


    def print_results(self):
        pass


    def print(self):
        self.game_board.test()
        self.game_board.print()

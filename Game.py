# !/usr/bin/python
# -*- coding: utf-8 -*-

import GameBoard
import Player

PLAYER_ONE = 0
PLAYER_TWO = 1

MESSAGE_TURN = "Your turn player %d"

TIE = None

class Game:
    def __init__(self, player_one, player_two):
        self.winner = None
        self.next_turn = PLAYER_ONE
        self.is_running = True
        self.choose_board = True
        self.last_board = None

        self.players = [Player.Player(*player_one), Player.Player(*player_two)]
        self.game_board = GameBoard.GameBoard()


    def __bool__(self):
        return self.is_running


    def next_move(self):
        piece = self.players[self.next_turn].piece
        has_winner = False
        while True:
            print(MESSAGE_TURN % (self.next_turn + 1))
            tic_tac_board = self.last_board
            if self.choose_board: # Update tic_tac_board
                tic_tac_board, pos = map(int, input("Please enter board and position: ").split())
            else:
                pos = map(int, input(
                    "Please enter position for board %d: " % self.last_board).split())

            # Checks if input is valid
            try:
                has_winner = self.game_board.move(piece, tic_tac_board, pos)
                print("Move added!\n\n")
                self.last_board = tic_tac_board
                break
            except IndexError as error:
                print(error)
            except ValueError as error:
                print(error)

        if has_winner:
            self.winner = self.next_turn
            self.is_running = False

        elif self.game_board.is_full:
            self.winner = TIE
            self.is_running = False

        self.next_turn = PLAYER_TWO if self.next_turn == PLAYER_ONE else PLAYER_ONE

    def print_results(self):
        if self.winner != TIE:
            print("Well done player %s on winning the game!\n\n"
                  % self.players[self.winner].name)
        else:
            print("We have a draw!\n\n")


    def print(self):
        self.game_board.test()
        self.game_board.print()

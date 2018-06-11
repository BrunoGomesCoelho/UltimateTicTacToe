import Game
from server import GameServer

PIECES = ["X", "O"]
MESSAGE_PLAY_AGAIN = "Would you like to play again? [y/n]: "
MESSAGE_CHANGE_PLAYERS = "Would you like to change players? [y/n]: "
MESSAGE_EXITING = "Thanks for playing! :)"

def main():
    game = Game.Game(("player 1", "X"), ("player 2", "O"))
    server = GameServer("127.0.0.1", 3001, game)

    server.start()

    print(MESSAGE_EXITING)


if __name__ == "__main__":
    main()

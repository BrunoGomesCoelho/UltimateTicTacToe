import Game, sys
from server import GameServer

MESSAGE_EXITING = "Thanks for playing! :)"

def main():
    game = Game.Game(("player 1", "X"), ("player 2", "O"))
    server = GameServer(sys.argv[1], int(sys.argv[2]), game)

    server.start()

    print(MESSAGE_EXITING)


if __name__ == "__main__":
    main()

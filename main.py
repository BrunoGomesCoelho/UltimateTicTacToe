import Game

PIECES = ["X", "O"]
MESSAGE_PLAY_AGAIN = "Would you like to play again? [y/n]: "
MESSAGE_CHANGE_PLAYERS = "Would you like to change players? [y/n]: "
MESSAGE_EXITING = "Thanks for playing! :)"


def get_name(player_id):
    name = input("Please write your name player %d: " % player_id)
    piece = PIECES[player_id - 1]
    print("Ok", name, "you will be '%c'!\n" % piece)
    return (name, PIECES)

def main():
    player_one = get_name(player_id=1)
    player_two = get_name(player_id=2)
    play_again = True

    while play_again:
        game = Game.Game(player_one, player_two)

        while game:
            game.next_move()
            print(game)

        game.print_results()
        play_again = True if input(MESSAGE_PLAY_AGAIN).rsplit() == "y" else False

        if play_again:
            change_players = True if input(MESSAGE_CHANGE_PLAYERS).rsplit() == "y" else False
            if change_players:
                player_one = get_name(player_id=1)
                player_two = get_name(player_id=2)

    print(MESSAGE_EXITING)


if __name__ == "__main__":
    main()

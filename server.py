import socket, sys, threading
import Game
import pickle

"""
The server waits for connections and handles games by controlling which
client should play in each turn
"""

class GameServer():
    def __init__(self, host, port, game):
        self.host = host
        self.port = port
        self.game = game

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()

        (self.player1, addr) = self.sock.accept()
        self.player1.send('1'.encode())
        self.player1.send(pickle.dumps(self.game))

        (self.player2, addr) = self.sock.accept()
        self.player2.send('2'.encode())
        self.player2.send(pickle.dumps(self.game))

        t = threading.Thread(target=self.play)
        t.start()


    def play(self):
        # send permission to play
        self.player1.send('.'.encode())

        while self.game:
            # get player1 play
            self.game = pickle.loads(self.player1.recv(4096))
            # send play1 to player2
            self.player2.send(pickle.dumps(self.game))
            # get player2 play
            self.game = pickle.loads(self.player2.recv(4096))
            # send play2 to player1
            self.player1.send(pickle.dumps(self.game))

        self.game.print_results()
        self.stop()

    def stop(self):
        self.player1.close()
        self.player2.close()



if __name__ == '__main__':
    server = GameServer(str(sys.argv[1]), int(sys.argv[2]))
    server.start()
    server.play()
    server.stop()

import socket, sys, threading
import Game
import pickle

"""
The client connects with the server and asks for a game with a specific
opponent (passing its IP address)
"""

class Client():
    def __init__(self, host, port, game = None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.player = None
        self.game = game

    def start(self):
        self.sock.connect((self.host, self.port))
        self.player = int(self.sock.recv(1024).decode())
        self.game = pickle.loads(self.sock.recv(4096))

        if(self.player == 1):
            print('You are the player 1')
        else:
            print('You are the player 2')

        t = threading.Thread(target=self.play)
        t.start()

    def play(self):
        if(self.player == 1):
            # wait for permission
            permission = self.sock.recv(1024).decode()
            # send first play
            self.game.next_move()
            self.game.print()
            self.sock.send(pickle.dumps(self.game))

        while self.game:
            # receive play
            self.game = pickle.loads(self.sock.recv(4096))
            self.game.print()

            self.game.next_move()
            self.game.print()
            self.sock.send(pickle.dumps(self.game))

        print('Game ended.')

    def stop(self):
        self.sock.close()

if __name__ == "__main__":
    client = Client(str(sys.argv[1]), int(sys.argv[2]))
    client.start()

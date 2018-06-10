import socket, sys, threading

"""
The server waits for connections and handles games by controlling which
client should play in each turn
"""

class GameServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.game_finished = False

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()

        (self.player1, addr) = self.sock.accept()
        self.player1.send('1'.encode())

        (self.player2, addr) = self.sock.accept()
        self.player2.send('2'.encode())

        t = threading.Thread(target=self.play)
        t.start()

        print('out')

    def play(self):
        print('in')
        while not self.game_finished:
            # send permission to play
            self.player1.send('.'.encode())
            # get player1 play
            play1 = self.player1.recv(1024).decode()
            # validate (valid play or game finished)
            #
            # send play1 to player2
            #
            # get player2 play
            play2 = self.player2.recv(1024).decode()
            # validate (valid play or game finished)
            #
            # send play2 to player1
            #

    def stop(self):
        self.game_finished = True
        self.player1.close()
        self.player2.close()



if __name__ == '__main__':
    server = GameServer(str(sys.argv[1]), int(sys.argv[2]))
    server.start()
    server.stop()

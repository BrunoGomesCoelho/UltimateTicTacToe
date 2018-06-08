import socket, sys, threading

"""
The client connects with the server and asks for a game with a specific
opponent (passing its IP address)
"""

class Client():
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.player = None
        self.game_finished = False

    def start(self):
        self.sock.connect((self.host, self.port))
        self.player = int(self.sock.recv(1024).decode())
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
            #

        while(not self.game_finished):
            # receive play
            message = self.sock.recv(1024).decode()
            # compute play
            #
            # send my play
            #



        print('Game ended.')

    def stop(self):
        self.game_finished = True
        self.sock.close()

if __name__ == "__main__":
    client = Client(str(sys.argv[1]), int(sys.argv[2]))
    client.start()

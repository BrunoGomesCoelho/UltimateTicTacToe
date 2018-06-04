import socket, sys

s = socket.socket()
host = socket.gethostname()
port = 5000

s.bind((host, port))



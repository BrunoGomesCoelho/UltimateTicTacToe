import socket, sys

s = socket.socket()
host = socket.gethostname()
port = 5001

s.bind((host, port))
s.listen(10)

while True:
    conn, addr = s.accept()
    print('Received connection from ' + str(addr))
    conn.send('Thanks for connecting')
    conn.close()

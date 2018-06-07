import sys, socket

# create an internet socket with stream type
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect with localhost on port 3000
sock.connect((socket.gethostname(), 3000))

# send data to connected host, remember to encode the data
sock.send('blabla'.encode())

# receive the data back from the server and print it
print(sock.recv(1024).decode())

sock.close()

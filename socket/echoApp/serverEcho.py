import sys, socket

# create socket form internet family of stream type
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# the socket refers to the host 127.0.0.1 on port 3000
#sock.bind(('127.0.0.1', 3000))
sock.bind((socket.gethostname(), 3000))
# this two lines make the same thing, but on the second one
# there is no hardcoding


# this allows the server to receive connections
sock.listen()



while True:

    # when a connection arrives, accept it
    # the accept method returns a socket object conn and the
    # incoming address
    (conn, address) = sock.accept()
    print('Just received a connection from' + str(address))


    # receive data from sender
    data = conn.recv(1024)


    # decode the data and print it
    print('Received data')
    print(data.decode('utf-8'))

    # send data back to client
    conn.send(data)

    conn.close()

sock.close()


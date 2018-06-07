# Socket

## Echo Application
The echo application is a well-commented code for exemplification of
socket usage as well as client-server architecture functioning. It is
really simple: the client sends some data to the server, the server
receives the data and sends it back to the client. Finally, the client
prints the data received (which is the same sent, the server doesn't
alter any of the data it receives from clients)


### Running
To run the application simply get the server up


> python3 serverEcho.py


Then use the `clientEcho.py` to send mesages to the server


> python3 clientEcho.py


You can also use the `clientEcho.py` to send data to any other server. Like
netcat. To do this, open a terminal session and execute netcat on listening
mode on port 3000 (the one `clientEcho.py` is programmed to send the data
to)


> nc -l -p 3000


Then execute the client


> python3 clientEcho.py


In this case, as `clientEcho.py` expects a response from the server, it
stops waiting for it. Typing anything on netcat and pressing enter sends
it to `clientEcho.py` and gets printed on the other terminal.

#!/usr/bin/env python
#copywright (c) Falon Scheers

import socket
import os
import sys
import select
#socket.AF_INET means socket on internet (IP)
#socket.SOCK_STREAM means TCP I think(?)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.S0L_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("0.0.0.0", 12345))
#0.0.0.0 specifies special number where we are going to go (IP to listen on) and all zeroes is all of them coming to the port 12345 in this case

serverSocket.listen(5) #means our program can be 5 requests behind or whatever.... 5 works

while True:
    print "Waiting for connection..."
    (incomingSocket, address) = serverSocket.accept()
    
    print "we got a connection from %s" % (str(address))
    pid = os.fork()
    if (pid == 0):
        #we must be in child process
        outgoingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        outgoingSocket.connect(("www.google.com", 80))
        request = bytearray()
        while True:
            incomingSocket.setblocking(0) #this prevents waiting and ending up in deadlock waiting for newline
            try:
                part = incomingSocket.recv(1024)
            except socket.error as exception:
                if exception.errno == 11:   #ignore if 11 because ....?
                    part = None
                else:               
                    raise
            if (part):
                request.extend(part)
                outgoingSocket.sendall(part)
                #clientSocket.sendall(part) #send back whatever we're recieving
         
            outgoingSocket.setblocking(0)
            try:
                part = outgoingSocket.recv(1024)
            except IOError, exception:
                if exception.errno == 11:   #ignore if 11 because ....?
                    part = None
                else:
                    raise
            if (part):
                incomingSocket.sendall(part)
            select.select([incomingSocket, outgoingSocket], [], [incomingSocket, outgoingSocket], 1)
    
        print request
        sys.exit(0)
    else:
        #we must be in the parent process so loop back around and wait for next connection
        pass

# after running need to do curl in another terminal to print anything:->   curl localhost:12345
# or telnet localhost 12345 to talk to ourselves.

#use proxy to act like a relay between two computers


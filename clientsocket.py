#!/usr/bin/env python
#copywright (c) Falon Scheers

import socket
#socket.AF_INET means socket on internet (IP)
#socket.SOCK_STREAM means TCP I think(?)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("www.google.com", 80))

request = "GET / HTTP/1.0\n\n"

clientSocket.sendall(request)

response = bytearray()
while True:
    part = clientSocket.recv(1024) #doesn't have to be 1024 but usually is or 2048
    if (part): 
        response.extend(part)
    else:
        break

print response

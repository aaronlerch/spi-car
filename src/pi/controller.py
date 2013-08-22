import socket
import sys
import select

try:
    print "import RPi.GPIO as GPIO"
except RuntimeError:
    print "Error importing RPi.GPIO"

PORT = 12000
BUFFER_SIZE = 1024
COMMANDS = ["STOP", "FORWARD", "REVERSE", "LEFT", "RIGHT", "STRAIGHT"]

address = ('', PORT)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)

print "Listening on port", PORT
server_socket.listen(1)

conn, addr = server_socket.accept()
print "Connection from", addr

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    data = data.strip()
    print "Received:", data
    response = "OK" if data in COMMANDS else "BAD COMMAND"
    conn.sendall(response)

conn.close()
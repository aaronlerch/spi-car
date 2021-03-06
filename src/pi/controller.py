#!/usr/bin/python

import socket
import sys
import select

try:
    print "import RPi.GPIO as GPIO"
except RuntimeError:
    print "Error importing RPi.GPIO"

PORT = 12000
BUFFER_SIZE = 1024
COMMANDS = ["STARTVIDEO", "STOPVIDEO", 
            "STOP", "FORWARD", "REVERSE", 
            "LEFT", "RIGHT", "STRAIGHT"]

def main(argv):
    address = ('', PORT)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)

    print "Listening on port", PORT
    server_socket.listen(1)

    conn, addr = server_socket.accept()
    print "Connection from", addr

    try:
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            data = data.strip().upper()
            if data in COMMANDS:
                response = "OK"
                print data
            else:
                response = "BAD_COMMAND"
            conn.sendall(response)
    except KeyboardInterrupt:
        pass
    finally:
        print "Stopping and straightening"
        conn.close()

if __name__ == "__main__":
   main(sys.argv[1:])
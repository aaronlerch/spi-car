#!/usr/bin/python

import socket
import sys
import select

PORT = 12000
BUFFER_SIZE = 1024

def main(argv):
    if len(argv) == 0:
        print "usage: test_spi.py [ip|hostname]"
        sys.exit()

    server = argv[0]
    address = (server, PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print "Connecting to spi-car at", server
    s.connect(address)

    print "Connected. Issue commands."
    
    try:
        cmd = raw_input().upper()
        while cmd != 'EXIT':
            s.sendall(cmd)
            data = s.recv(BUFFER_SIZE)
            if not data: break
            print data
            cmd = raw_input().upper()
    finally:
        s.close()
        print "Disconnected"

if __name__ == "__main__":
   main(sys.argv[1:])
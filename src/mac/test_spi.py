#!/usr/bin/python

import socket
import tty, sys, termios
import select

PORT = 12000
BUFFER_SIZE = 1024
COMMANDS = {
                "a" : "LEFT",
                "d" : "RIGHT",
                "w" : "FORWARD",
                "s" : "REVERSE",
                "x" : "STOP",
           }

# All commands:
# ["STARTVIDEO", "STOPVIDEO", "STOP", "FORWARD", "REVERSE", "LEFT", "RIGHT", "STRAIGHT"]

def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main(argv):
    if len(argv) == 0:
        print "usage: test_spi.py [ip|hostname]"
        sys.exit()

    server = argv[0]
    address = (server, PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print "Connecting to spi-car at", server
    s.connect(address)

    print "Connected. Issue commands!"
    
    try:
        cmds = {
                "a" : lambda: sys.stdout.write("LEFT"),
                "d" : lambda: sys.stdout.write("RIGHT")
               }

        ch = getchar()
        if cmds.has_key(ch):
            cmds[ch]()

        #cmd = raw_input().upper()
        #while cmd != 'EXIT':
        #    s.sendall(cmd)
        #    data = s.recv(BUFFER_SIZE)
        #    if not data: break
        #    print data
        #    cmd = raw_input().upper()
    finally:
        s.close()
        print "Disconnected"

if __name__ == "__main__":
   main(sys.argv[1:])
from socket import *
import sys
import select
address = ('', 12001)
server_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(address)

# From: http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
disco_s = socket(AF_INET, SOCK_DGRAM)
disco_s.connect(("8.8.8.8",80))  # 8.8.8.8 is the google DNS server address itself
local_ip = disco_s.getsockname()[0]
disco_s.close()

print "Local IP is " + local_ip

while (1):
    recv_data, addr = server_socket.recvfrom(2048)
    print "Received request from " + addr[0]
    server_socket.sendto(local_ip, addr)

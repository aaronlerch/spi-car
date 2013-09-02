#!/bin/sh

echo "hi" | socat - UDP-DATAGRAM:255.255.255.255:12001,broadcast

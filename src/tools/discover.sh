#!/bin/sh

echo "hi" | socat - UDP-DATAGRAM:255.255.255.255:12101,broadcast

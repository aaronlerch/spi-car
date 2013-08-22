#!/bin/sh

echo "Starting h.264 video stream on port 5000"
LOCAL_IP=`ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'`
raspivid -t 0 -h 240 -w 320 -fps 15 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=$LOCAL_IP port=5000

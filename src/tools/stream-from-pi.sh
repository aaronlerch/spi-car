#!/bin/sh

PI_ADDR=`echo "hi" | socat - UDP-DATAGRAM:255.255.255.255:12101,broadcast`
if [ -z "$PI_ADDR" ];
then
  echo "Unable to find a Raspberry Pi on the local network. Either the discovery PONG app isn't running, or it doesn't exist!"
  exit 1
fi

echo "Receiving stream from the Pi found at $PI_ADDR:5000"
gst-launch-1.0 -v tcpclientsrc host=$PI_ADDR port=5000 ! gdpdepay !  rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false

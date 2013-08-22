# Spi Car

 (Get it? Raspberry Pi Spy Car)

A Raspberry Pi-driven RC car that my son (7) and daughter (9) and I are building.

## Objective

A SIMPLE project that spans a gamut of concepts between programming and electronics, with a 
(hopefully) sweet payout at the end. This should be something we can accomplish in a moderate 
amount of time with limited resources and above all else, it should be SIMPLE. Did I mention SIMPLE?

## High level idea

We want to install a battery-driven Raspberry Pi and camera onto an existing RC car and use the GPIO 
pins to control forward/reverse and left/right. The Pi should be discoverable without knowing the IP address
ahead of time (assuming connected to the same router), and it should expose a realtime streaming video 
endpoint as well as a simple API to control the car.

At the start, the controller will be software running on a laptop, with plans to implement an iOS app
to expose the video and simple controls.

## Components & Software

Components

* Raspberry Pi, including
  * Raspberry Pi camera board
  * Micro wifi dongle
  * Portable battery pack (TBD)
  * Camera mount (off-the-shelf possible, I'd like to 3D print a custom one -- so far TBD)
* RC car - we bought a $20 car from Fry's, similar to this one: http://www.frys.com/product/7257233
* Wiring between GPIO pins and car's circuit board

Software

* GStreamer for streaming realtime h.264 video
* Network discovery app (Python app, listens for broadcast UDP and responds with the Pi's IP address)
* API app on the Pi (Python? C? Ruby? HTTP-based or TCP sockets?)

## Questions

Does the API need to require a persistent connection? How else would we handle "drive forward" in a 
way that doesn't end up with the car forced into always driving forward (or only driving forward in 
short bursts). A web-based controller would be cool.

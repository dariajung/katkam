katkam
======

A way to keep an eye on your cat whilst away from home.

[Kam](http://katkam.herokuapp.com)

####Hardware Components
----
Katkam is built using a Raspberry Pi. The Pi is used for starting a web server and streaming video from the PS3Eye USB Webcam to a local port. Eventually, there will be a servo and laser pointer toy component for playing with your cat remotely.

####Libraries used on the Pi
-----

The Motion and ffmpeg libraries are used to enable video streaming. Motion allows for snapshots to be taken when there is movement detected in front of the webcam.

####Other things:
---
The web app is built using Flask, Python, and is hosted on Heroku. Ngrok is used to create a tunnel from the localhost streaming from the Pi to the Internet so the video feed can be viewable from outside of the Pi's local network.

####Resources
___

- [Setting up motion](http://chris.gg/2012/07/using-a-ps3-eyetoy-with-the-raspberry-pi/)

####LICENSE
MIT


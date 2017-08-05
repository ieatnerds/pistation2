"""
Author(s): Nicholas Kelly(importantnk@gmaail.com)
Date: July 10th, 2017

PiStation2 - Update Script

This script will be used to auto update the PiStation2 when the eject button
is pressed. It will also cause the blue LED of the eject button to light up
until the update is over.

This makes system calls to apt-get in order to update the Pi
in every way I could think.
"""

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)  # This pin controls a transistor for the LED.

while True:
    input_state = GPIO.input(26)
    if input_state is False:
        GPIO.output(21, GPIO.HIGH)
        os.system("sudo apt-get update")
        os.system("sudo apt-get -y upgrade")
        os.system("sudo apt-get -y dist-upgrade")
        os.system("sudo apt-get -y install rpi-update")
        GPIO.output(21, GPIO.LOW)
    time.sleep(.2)

"""
Nicholas Kelly
update script

This script will be used to autpo update the pistation2
it will also cause the blue ledd to light up until the update is
over.

this makes systmem calls to apt-get in order to update the machine
in every way I could think.
"""

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)

while True:
    input_state = GPIO.input(26)
    if input_state == False:
        GPIO.output(21, GPIO.HIGH)
        os.system("sudo apt-get update")
        os.system("sudo apt-get -y upgrade")
        os.system("sudo apt-get -y dist-upgrade")
        os.system("sudo apt-get -y install rpi-update")
        GPIO.output(21, GPIO.LOW)
        print('Done.')
    time.sleep(.2)
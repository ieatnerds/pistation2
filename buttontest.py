"""
Author(s): Nicholas Kelly(importantnk@gmaail.com)
Date: July 10th, 2017
GPIO Test - Button test

This program will simply print a statement if an input is detected on a
gpio pin. for the purposes we are currently using this will involve the
GPIO 04 pin
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state is False:
        print('A button has been pressed.')
    time.sleep(.2)

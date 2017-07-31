"""
Nicholas Kelly
Button test

This program will simply print a statement if an input is detected on a
gpio pin. for the pursposes we are currently using this will involve the
GPIO 04 pin
"""

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        os.system('shutdown -r now')
    time.sleep(.2)
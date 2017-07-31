"""
Nicholas Kelly
Power script

This script is used to restart the pistation2

this will keep the green led on while the pistation is operating
and then switch to the red led after the button is pressed until
shutdown.
"""

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM) 

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(20, GPIO.HIGH)
while True:
    input_state = GPIO.input(19)
    if input_state is False:
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        os.system('sudo reboot')
    time.sleep(.2)

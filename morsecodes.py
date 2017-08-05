"""
Author(s): Nicholas Kelly(importantnk@gmaail.com)
Date: July 10th, 2017

GPIO Test - MorseCode

This program/ script will help in testing the GPIO pins on my
my raspberry pi. It will send power through a specified pin as
morse code.
"""
# Imports
import RPi.GPIO as GPIO
import time as t

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

# Dictionary
d = {'a':('short', 'long'), 'b':('long', 'short', 'short', 'short'),
     'c':('long','short', 'long', 'short'), 'd':('long', 'short', 'short'),
     'e':('short',), 'f':('short', 'short', 'long', 'short'),
     'g':('long','long', 'short'), 'h':('short', 'short', 'short', 'short'),
     'i':('short', 'short'), 'j':('short', 'long', 'long', 'long'),
     'k':('long', 'short', 'long'), 'l':('short', 'long', 'short', 'short'),
     'm':('long', 'long'), 'n':('long', 'short'), 'o':('long', 'long', 'long'),
     'p':('short', 'long', 'long', 'short'), 'q':('long', 'long', 'short', 'long'),
     'r':('short', 'long', 'short'), 's':('short', 'short', 'short'),
     't':('long',), 'u':('short', 'short', 'long'),
     'v':('short', 'short', 'short', 'long'), 'w':('short', 'long', 'long'),
     'x':('long', 'short', 'short', 'long'), 'y':('long', 'short', 'long', 'long'),
     'z':('long', 'long', 'short', 'short'), ' ':('slash',), '.':('slash',),
     '?':('slash',), ',':('slash',), "'":('slash',)}


# Functions
def on():
    """Define pin on."""
    GPIO.output(18, GPIO.HIGH)


def off():
    """Define pin off."""
    GPIO.output(18, GPIO.LOW)


def short():
    """Define what a short beep will be."""
    on()
    print('.')
    t.sleep(.5/2)
    off()
    t.sleep(.5/2)


def long():
    """Define what a long beep will be."""
    on()
    print('-')
    t.sleep(1/2)
    off()
    t.sleep(.5/2)


def slash():
    """Define in between words."""
    print('/')
    t.sleep(2.5/2)


def find(letter):
    """Find letter in dictionary."""
    lst = d[letter]
    return lst


def printletter(lst):
    """Displays a letter of morse code."""
    print(lst)
    for code in lst:
        if code == 'short':
            short()
        elif code == 'long':
            long()
        else:
            slash()


def breakdown(text):
    """
    This will take the list of short and long beeps given from the dictionary,
    and then calls the printletter function.
    """
    for item in text:
        code = find(item.lower())
        printletter(code)


def main():
    """
    Gets user input an then prints it as morse code
    through the gpio pins.
    """
    off()
    text = input('Please enter a message to be read in morse code.')
    breakdown(text)

    input('Press enter to exit.')
    GPIO.cleanup()

main()

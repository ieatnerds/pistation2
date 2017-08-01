"""
Nicholas Kelly
GPIO Test

This program/ script will help in testing the GPIO pins on my
my raspberry pi. It will send power through a specified pin as
morse code
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
    """define pin on."""
    GPIO.output(18, GPIO.HIGH)


def off():
    """define pin off."""
    GPIO.output(18, GPIO.LOW)


def short():
    """define what a short beep will be."""
    on()
    print('.')
    t.sleep(.5/2)
    off()
    t.sleep(.5/2)


def long():
    """define what a long beep will be."""
    on()
    print('-')
    t.sleep(1/2)
    off()
    t.sleep(.5/2)


def slash():
    """define in between words."""
    print('/')
    t.sleep(2.5/2)


def find(letter):
    """find letter in dictionary."""
    lst = d[letter]
    return lst


def printletter(lst):
    """"""
    print(lst)
    for code in lst:
        if code == 'short':
            short()
        elif code == 'long':
            long()
        else:
            slash()


def breakdown(text):
    for item in text:
        code = find(item.lower())
        printletter(code)


def main():
    """gets user input an then prints it as morse code
    through the gpio pins."""
    off()
    text = input('Please enter a message to be read in morse code.')
    breakdown(text)

    input('Press enter to exit.')
    GPIO.cleanup()

main()

#Traffic light
########################### Matt's Sources ##################################
# Das Blinkenlights references
# google://blink led python raspberry-pi
# https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/
# https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
# For curses references...
# google://non-blocking keyboard read python
# https://ubuntuforums.org/showthread.php?t=1514035
#############################################################################
import pibrella

import datetime
from datetime import timedelta
import RPi.GPIO as GPIO
import  curses, \
        time


####Setup##########
GREENPIN  = 4
YELLOWPIN = 5
REDPIN = 6
time_of_press = []
current_light = "green"
button_pressable = True



def get_key (win):
    key = None
    try:
        key = win.getkey()
    except:
        pass
    return key


def button_pushed(win):
    k = get_key(win)
    if k == " ":
        return 1
    else:
        return 0


#Where the change of lights happen
def loop (win):
    k = get_key(win)
    if k == "q":
        return -1
    else:
        if button_pushed(win) == 1 and current_light == "green" and button_pressable == True:
            button_pressable = False
            time_of_press = datetime.datetime.now().time()+timedelta(seconds=3)
        current_time = datetime.datetime.now().time()
        if current_time <= time_of_press and button_pressable == False:
            if current_light == "green":
                current_light = "yellow"
                GPIO.output(GREENPIN, GPIO.LOW)
                GPIO.output(YELLOWPIN, GPIO.HIGH)
                print "Yellow"
                time_of_press = datetime.datetime.now().time()+timedelta(seconds=3)
            elif current_light == "yellow":
                current_light = "red"
                GPIO.output(YELLOWPIN, GPIO.LOW)
                GPIO.output(REDPIN, GPIO.HIGH)
                print "Red"    
                time_of_press = datetime.datetime.now().time()+timedelta(seconds=5)
            elif current_light == "red":
                current_light = "waiting"
                GPIO.output(REDPIN, GPIO.LOW)
                GPIO.output(GREENPIN, GPIO.LOW)
                time_of_press = datetime.datetime.now().time()+timedelta(seconds=10)
            elif current_light == "waiting":
                current_light = "green"
                button_pressable = True
            else:
                print "error in current time comparison"
    return 0


def setup (win):
    RUNNING = True
    win.nodelay(True) 
    win.clear()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GREENPIN, GPIO.OUT)
    GPIO.setup(YELLOWPIN, GPIO.OUT)
    GPIO.setup(REDPIN, GPIO.OUT)
    GPIO.output(GREENPIN, GPIO.HIGH)
  #While true loop. 
    while RUNNING:
        exit_code = loop(win)
        if exit_code < 0:
            RUNNING = False


if __name__ == "__main__":
    curses.wrapper(setup)
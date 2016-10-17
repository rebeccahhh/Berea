import RPi.GPIO as GPIO
import  curses, \
        time

# Configuration variables.
GREENPIN  = 4

def get_key (win):
  key = None
  try:
    key = win.getkey()
  except:
    pass
  return key

# Das Blinkenlights references
# google://blink led python raspberry-pi
# https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/
# https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

def loop (win):
  k = get_key(win)
  if k == "q":
    return -1
  else:
    print "LED on\r"
    GPIO.output(GREENPIN, GPIO.HIGH)
    time.sleep(1)
    print "LED off\r"
    GPIO.output(GREENPIN, GPIO.LOW)
    time.sleep(1)
    return 0

def setup (win):
  RUNNING = True
  win.nodelay(True) 
  win.clear()

  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(GREENPIN, GPIO.OUT)
  # When we are done setting up, loop. 
  while RUNNING:
    # Our loop function happens over and over.
    # It isn't a loop so much as the "body" of
    # the 
    exit_code = loop(win)
    # If we get a return value less than zero,
    # We should stop looping. Set RUNNING to False.
    if exit_code < 0:
      RUNNING = False

# For curses references...
# google://non-blocking keyboard read python
# https://ubuntuforums.org/showthread.php?t=1514035
if __name__ == "__main__":
  curses.wrapper(setup)
  

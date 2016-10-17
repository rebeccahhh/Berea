######################################################################
# Author: Dr. Jan Pearce  ****** CHANGE THIS!! ******
# username: pearcej ****** CHANGE THIS!! *****

# Assignment: L1 Steganography
# Purpose: To encode a secret message that is very secret.
######################################################################
# Acknowledgements:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

# You need to acknowledge having modifed this code and all other code you modify or use for assitance.
#   To do so, you will indicate something like:
#   Mopidied from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-A15.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################

from ppm import *
# Be sure you work with a single ppm object at a time

# The following interaction is just for testing.  You will improve this.
run = PPM_set_up()
filename=raw_input("Please input name of PPM-P3 file:")
ppmobject=PPM(run,filename)
#ppmobject=PPM() also works

# The following is a very small image list which differs from the default image
testlist=[[[0, 0, 255], [0, 255, 0], [0, 30, 30]],
[[40, 40, 40], [50, 50, 50],[60, 60, 60]]]

edits=raw_input("do you want to update from list?")
if edits=='y' or edits=='Y':
    ppmobject.PPM_updatefrompixellist(testlist)

edits=raw_input("do you want to turn red?")
if edits=='y' or edits=='Y':
    ppmobject.PPM_make_red()


root.mainloop() #needed to use Tkinter with the ppm class
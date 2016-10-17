# simulation.py
#
# modified from code by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

# modifications are all of the print statements in the main()

from random import random, randrange
from CheckerSim import CheckerSim
from myQueue import Queue

class Customer(object):

    def __init__(self, arrivalTime, itemCount):
        self.arrivalTime = int(arrivalTime)
        self.itemCount = int(itemCount)

    def __repr__(self):
        return ("Customer(arrivalTime=%d, itemCount=%d)" %
                (self.arrivalTime, self.itemCount))


def genTestData(filename, totalTicks, maxItems, arrivalInterval):
    outfile = open(filename, "w")
    # step through the ticks
    for t in range(1,totalTicks):
        if random() < 1./arrivalInterval:
            # a customer arrives this tick
            # with a random number of items
            items = randrange(1, maxItems+1)
            outfile.write("%d %d\n" % (t, items))
    outfile.close()

def createArrivalQueue(fname):
    q = Queue()
    infile = open(fname)
    for line in infile:
        time, items = line.split()
        q.enqueue(Customer(time,items))
    infile.close()
    return q

def main():
    print("This simulation is a simple model of the check-out process.")
    print("Each line of our data contains an arrivalTime followed by an itemCount.")
    genTestData("checkerData.txt", 3*60*60, 50, 120)
    q = createArrivalQueue("checkerData.txt")
    sim = CheckerSim(q, 3)
    sim.run()
    print("")
    print("Average wait time: ")
    print (sim.averageWait())
    print("Maximum wait time: ")
    print (sim.maximumWait())
    print("Maximum line length: ")
    print (sim.maximumLineLength())

if __name__ == '__main__':
    main()

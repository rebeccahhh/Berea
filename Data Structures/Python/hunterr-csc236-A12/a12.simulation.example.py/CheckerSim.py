# CheckerSim.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

from myQueue import Queue

class CheckerSim(object):

    #------------------------------------------------------------

    def __init__(self, arrivalQueue, avgTime):
        self.time = 0                # ticks so far in simulation
        self.arrivals = arrivalQueue # queue of arrival events to process
        self.line = Queue()          # customers waiting in line
        self.serviceTime = 0         # time left for current customer
        self.totalWait = 0           # sum of wait time for all customers
        self.maxWait = 0             # longest wait of any customer
        self.customerCount = 0       # number of customers processed
        self.maxLength = 0           # maximum line length
        self.ticksPerItem = avgTime  # time to process an item

    #------------------------------------------------------------

    def run(self):
        while (self.arrivals.size() > 0 or
               self.line.size() > 0 or
               self.serviceTime > 0):
            self.clockTick()

    #------------------------------------------------------------

    def averageWait(self):
        return float(self.totalWait) / self.customerCount

    #------------------------------------------------------------

    def  maximumWait(self):
        return self.maxWait

    #------------------------------------------------------------

    def maximumLineLength(self):
        return self.maxLength

    #------------------------------------------------------------

    def clockTick(self):
        # one tick of time elapses
        self.time += 1

        # customer(s) arriving at current time enter the line
        while (self.arrivals.size() > 0 and
               self.arrivals.front().arrivalTime == self.time):
            self.line.enqueue(self.arrivals.dequeue())
            self.customerCount += 1
        # if line has reached a new maximum, remember that
        self.maxLength = max(self.maxLength, self.line.size())

        # process items
        if self.serviceTime > 0:
            # a customer is currently being helped
            self.serviceTime -= 1
        elif self.line.size() > 0:
            # help the next customer in line
            customer = self.line.dequeue()
            #print self.time, customer      # nice tracing point
            # compute and update statistics on this customer
            self.serviceTime = customer.itemCount * self.ticksPerItem
            waitTime = self.time - customer.arrivalTime
            self.totalWait += waitTime
            self.maxWait = max(self.maxWait, waitTime)

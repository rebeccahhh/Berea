# test_Markov.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014
#
# Modified by Jan Pearce, Sept. 7, 2014
#  - local variable "model" in the makeWordModel function was renamed to "tmpmodel"
#    to avoid confusion with "model" instance variable in class Markov
#  - input() function is replaced with raw_input() to conform with Python 2.7
# Modified by Mario Nakazawa, Sept. 7, 2014
#  - added docstrings to both functions

from Markov import Markov

def makeWordModel(filename):
    '''creates a Morkov model from the words in the file with filename.
    pre: The file with name filename exists.
    post: A Markov chain from the text in the file is returned. '''
    # creates a Markov model from words in filename
    infile = open(filename)
    tmpmodel = Markov()
    for line in infile:
        words = line.split()
        for w in words:
            tmpmodel.add(w)
    infile.close()
    # Add a sentinel at the end of the text
    tmpmodel.add(None)
    tmpmodel.reset()
    return tmpmodel

def generateWordChain(markov, n):
    ''' generates up to n words on output from the model "markov"
    pre: markov is a valid Markov chain where the length is longer than "n"
    post: a string of n words will be returned using the Markov chain.'''
    # generates up to n words of output from a model
    words = []
    for i in range(n):
        next = markov.randomNext()
        if next is None: break  # got to a final state
        words.append(next)
    return " ".join(words)

#main
fname = raw_input('enter filename: ')
m = makeWordModel(fname)
print(generateWordChain(m, 50))
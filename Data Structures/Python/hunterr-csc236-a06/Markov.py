# Markov.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

import random

class Markov(object):
    
    """A simple trigram Markov model.  The current state is a sequence
       of the two words seen most recently. Initially, the state is
       (None, None), since no words have been seen. Scanning the
       sentence "The man ate the pasta" would cause the
       model to go through the sequence of states: [(None,None),
       (None, 'The'), ('The', 'man'), ('man','ate'), ('ate','the'),
       ('the','pasta')]"""

    #------------------------------------------------------------

    def __init__(self):
        
        """post: creates an empty Markov model with initial state
                 (None, None)."""

        self.model = {}  # maps states to lists of words
        self.state = (None, None)  # last two words processed


    #------------------------------------------------------------

    def add(self, word): 
        
        """post: Adds word as a possible following word for current
                 state of the Markov model and sets state to
                 incorporate word as most recently seen.

           ex: If state was ("the", "man") and word is "ate" then
               "ate" is added as a word that can follow "... the man" and
               the state is now ("man", "ate")"""

        if self.state in self.model:
            # we have an existing list of words for this state
            # just add this new one (word).
            self.model[self.state].append(word)
        else:
            # first occurrence of this state, create a new list
            self.model[self.state] = [word]
        # transition to the next state given next word
        self._transition(word)

    #------------------------------------------------------------

    def randomNext(self):

        """post: Returns a random choice from among the possible choices
                 of next words, given the current state, and updates the 
                 state to reflect the word produced.

           ex: If the current state is ("the", "man"), and the known
               next words are ["ate", "ran", "hit", "ran"], one of
               these is selected at random. Suppose "ran" is selected,
               then the new state will be: ("man", "ran"). Note the
               list of next words can contain duplicates so the
               relative frequency of a word in the list represents its
               probablility of being the next word."""

        # get list of next words for this state
        lst = self.model[self.state]
        # choose one at random
        choice = random.choice(lst)
        # transition to next state, given the word choice
        self._transition(choice)
        return choice

    #------------------------------------------------------------

    def _transition(self, next):

        """post: sets the state based on the 'next' word"""
        
        # help function to construct next state
        self.state = (self.state[1], next)

    #------------------------------------------------------------

    def reset(self):

        """post: The model state is reset to its initial 
        (None, None) state.

           note: This does not change the transition information that
                 has been learned so far (via add()), it
                 just resets the state so we can start adding
                 transitions or making predictions for a "fresh"
                 sequence."""

        self.state = (None, None)
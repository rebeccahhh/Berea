from Stack import Stack
from Queue import Queue
import random
import sys

class War():
    def __init__(self):
        self.myCurrent	= None	# my currently displayed card
        self.otherCurrent = None	# other currently displayed card
        self.currentState = None	# keeps track of the state of play
        self.dealingPile = Stack()
        self.myPayingPile = Stack()	#Nice Spelling
        self.otherPlayingPile = Stack()
        self.myStoragePile = Queue()
        self.otherStoragePile = Queue()
        self.lootPile = Queue()
        
    def add_dealing(self):
        '''Makes all of the cards possible for the game
        pre: nothing
        post: returns a shuffled list of the possible cards'''
        deck = []
        #we did this two for loops to do the shuffling
        for i in range(5):
            for i in range(10):
                deck.append(i)
        random.shuffle(deck)
        #print deck
        for i in range(len(deck)):
            self.dealingPile.push(deck[i])
        return deck

    def deal(self):
        '''Places the deck into two different stacks
        if action was sucessful should return true'''
        length = self.dealingPile.size() #use .size() to get the size of the stack
        for i in range(length):
            card = self.dealingPile.pop()
            if i%2 == 0:
                self.myPayingPile.push(card)
            else:
                self.otherPlayingPile.push(card)
        return True

    def make_move(self):
        '''Monitors each round of the game. Checking for storage size of your pile and the opponents pile. Also checks to see if the game should stop.'''
        stop = False
        while stop == False:
            while self.myPayingPile.size() != 0 and self.otherPlayingPile.size() != 0:
                self.compare_card()
            if self.myPayingPile.size() == 0:
                stop = self.move_my_storage()
            else:
                stop = self.move_other_storage()
        return 0

    def remove_my_card(self):
        '''Adjust the current card depending off of what is poped from player 1 playing hand and adds it to the loop pile if the size of their playing hand is not 0
        if it is zero it will return false.'''
        if self.myPayingPile.size() != 0:
            self.myCurrent = self.myPayingPile.pop()
            self.lootPile.enqueue(self.myCurrent)
        else:
            return False

    def remove_other_card(self):
        '''Adjust the current card depending off of what is poped from player 2 playing hand and adds it to the loop pile if the size of their playing hand is not 0
        if it is zero it will return false.'''
        if self.otherPlayingPile.size() != 0:
            self.otherCurrent = self.otherPlayingPile.pop()
            self.lootPile.enqueue(self.otherCurrent)
        else:
            return False

    def compare_card(self):
        '''Makes adjustments for every possible outcome when comparing player 1 and player 2's cards. Will move the loot of the player who won or will call a function for if they are the same'''
        self.remove_my_card()
        self.remove_other_card()
        print 'player one card is ' + str(self.myCurrent)
        print 'player two card is ' + str(self.otherCurrent)
        print '                                                    '
        if self.myCurrent > self.otherCurrent:
            self.move_my_loot()
            #return (True,'my loot')
        elif self.myCurrent < self.otherCurrent:
            self.move_other_loot()
            #return (True,'other loot')
        else:
            self.goingtowar()
            #return 'war'
        return 0

    def goingtowar(self):
        '''called when player 1 and player 2 have the same card. removes the next card if there are cards to remove then calls the compare function'''
        x = self.remove_my_card()
        y = self.remove_other_card()
        if x == False:
            print 'it happened for x'
        elif y == False:
            print 'it happend for y'
        else:
            self.compare_card()

    def move_my_loot(self):
        '''move everything from lootpile to player's 1 storage pile'''
        length = self.lootPile.size()
        for i in range(length):
            card = self.lootPile.dequeue()
            self.myStoragePile.enqueue(card)
        return self.myStoragePile

    def move_other_loot(self):
        '''moves everything from lootpile to player's 2 storage pile'''
        length = self.lootPile.size()
        for i in range(length):
            card = self.lootPile.dequeue()
            self.otherStoragePile.enqueue(card)
        return self.otherStoragePile

    def move_my_storage(self):
        '''moves player ones storage pile to their playing pile if the storage pile is not empty, then returns False. If it is empty the function will return True and indicate that the player has lost'''
        length = self.myStoragePile.size()
        if length != 0:
            for i in range(length):
                card = self.myStoragePile.dequeue()
                self.myPayingPile.push(card)
            return False
        else:
            print 'player 1 has lost'
            return True

    def move_other_storage(self):
        '''moves player ones storage pile to their playing pile if the storage pile is not empty, then returns False. If it is empty the function will return True and indicate that the player has lost'''
        length = self.otherStoragePile.size()
        if length != 0:
            for i in range(length):
                card = self.otherStoragePile.dequeue()
                self.otherPlayingPile.push(card)
            return False
        else:
            print 'player 2 has lost'
            return True



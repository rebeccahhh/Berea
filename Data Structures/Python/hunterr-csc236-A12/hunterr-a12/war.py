from Stack import Stack
import Queue
from Queue import Queue
import random

class War:
    def __init__(self):	  
        # possibly useful instance variables
        self.myCurrent = None		# my currently displayed card
        self.otherCurrent = None	# other currently displayed card
        self.currentState = 0	# keeps track of the state of play
        self.dealingPile = Stack()	# queue or stack
        self.myHand = Stack()	# queue or stack 
        self.myStorage = Queue()	# queue or stack
        self.compHand = Stack()	# queue or stack    
        self.compStorage = Queue()	# queue or stack
        self.lootPile = Queue()		# queue or stack

    #def War():??
    # Constructor initializes all instance variables

    def add_dealingPile(self):
        suit=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for i in range(4):
            for i in suit:
                self.dealingPile.push(i)
        random.shuffle(self.dealingPile.items)
        print self.dealingPile.items
        return self.dealingPile
    
    def deal(self):
    # deals out 25 cards from to each player's playing pile from shuffled dealers pile
        count = 0
        while count < 25:
            x = self.dealingPile.pop()
            self.myHand.push(x)
            y = self.dealingPile.pop()
            self.compHand.push(y)
            count + 1
        self.state = 1
        
        # self.myPlayingPile.push(self, object)
    
    def make_move(self):
    # initiates a round of play and communicates play-by-play during the round
    # returns true when the game is still in play
    # returns false when the game is over
    # Communicates an appropriate message about whether the user beat the computer
        while self.state == 1:
            while self.myHand.size() != 0 and self.compHand.size() != 0:
                my = self.myHand.pop()
                comp = self.compHand.pop()
                self.compare_cards(my, comp)
                if self.myHand.size() == 0:
                    self.move_my_storage()
                elif self.compHand.size() == 0:
                    self.move_comp_storage()
                else:
                    self.state = 0
            if self.state == 0:
                #compare total cards
                print("You need to do something here Becca")
            print()
    
    def remove_my_card(self):
    # Precondition: myPlayingPile is not empty 
    # If it is not empty, the function removes a card from myPlayingPile, 
    # returning the stored value 
        if self.myHand != None:
            card = self.myHand.pop()
            self.lootPile.enqueue(card)
            #return self.lootPile()
        else:
            print("What in tarnation???")
        
    def remove_other_card(self):
    # Precondition: compHand is not empty 
    # If it is not empty, the function removes a card from compHand,
    # returning the stored value
        if self.compHand != None:
            card = self.compHand.pop()
            self.lootPile.enqueue(card)
            #return self.lootPile()
        else:
            print("dag-flabbit")

    
    def compare_cards(self, my, comp):
    # compares myCurrent to otherCurrent and behaves appropriately     
        my = my
        comp = comp
        print str(my)
        print str(comp)
        if my > comp:
            self.lootPile.enqueue(my)
            self.lootPile.enqueue(comp)
            self.move_my_loot()
            
        elif my < comp:
            self.lootPile.enqueue(my)
            self.lootPile.enqueue(comp)
            self.move_other_loot()
            
        elif my == comp:
            self.state = 1
        else:
            print ("HELP MEEEE")
            
    def move_my_loot(self):
    # moves everything from lootPile to myStorage  
        loot = self.lootPile.size()
        for i in range(loot):
            self.lootPile.dequeue()
            self.myStorage.enqueue(i)
    # does this work????
            
    def move_other_loot(self):
    # moves everything from lootPile to compStorage
        loot = self.lootPile.size()
        for i in range(loot):
            self.lootPile.dequeue()
            self.compStorage.enqueue(i)
    
    def move_my_storage(self):
    # moves everything from myStorage to myPlayingPile
        stuff = self.myStorage.size()
        for i in range(stuff):
            self.myStorage.dequeue()
            self.myHand.push(i)
    
    def move_comp_storage(self):
    # moves everything from compStorage to compHand
        for i in self.compStorage():
            self.compStorage.dequeue()
            self.compHand.push(i)
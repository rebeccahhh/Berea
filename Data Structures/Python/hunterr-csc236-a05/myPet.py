################################################################################
# Purpose: to create a fun and rewarding virtual pet for a programmer to interact with.
# Perfect for the person who is allergic to everything and can't have real pets...
# Author: Rebeccah Hunter
# Acknowledgments: Berea College Computer Science Department and Dr. Mario Nakazawa
################################################################################
from BasicPet import BasicPet
from petSurprise import petSurprise

def begin(Seymour):
    '''This function is the starting section of the virtual pet game.
    It should utilise the user's input to move on the the next part of game play.
    '''
    user_input = raw_input("Hello, would you like to care for a virtual pet? \nPlease type y or n to take on this non-existant pet named Seymour")
    user_input = user_input.lower()

    if user_input == "y":
        print ("Great! You must care for Seymour in 3 ways. 1 is to give your pet sustenance.\n2 is to do activity and boost metabolism.3 is to love your pet.\nYou may enter n to leave:")
    elif user_input == "n":
        print ("you cold hearted, neglectful individual. How could you abandon \nthis tiny fake virtual robot-pet? You're a monster!")
        Seymour.dragonAttack()
    else:
        print ("I'm so sorry, something went wrong. Perhaps your pet was eaten\
        by a dragon, or perhaps you were..")

    
def care():
    '''A function to determines the user's care choice for their pet.
    '''
    caring = raw_input("Please enter 1, 2, or 3 to care for your pet.")
    return caring


def continueCare(Audrey, Seymour):
    '''A function to determine whether the gameplay continues or not.
    '''
    yes_check = raw_input("would you like to continue to care for your pet?\nEnter y or n: ")
    check = yes_check.lower()
    return check


def main():
    '''Audrey is an instance of BasicPet and Seymour the instance of a dragon attack.
    '''
    Seymour = petSurprise()
    Audrey = BasicPet()
    begin(Seymour)
    checked = continueCare(Audrey, Seymour)
    while checked == "y":
        caring = care()
        if caring == "1":
            Audrey.feedMe()
            Audrey.checkPet()
        elif caring == "2":
            Audrey.walkMe()
            Audrey.checkPet()
        elif caring == "3":
            Audrey.loveMe()
            Audrey.checkPet()
        elif caring == "n":
            Audrey.neglectMe()
            Audrey.checkPet()
            if Audrey.neglect == 0:
                Seymour.dragonAttack()
        else:
            print "Feed Me!"
        checked = continueCare(Audrey, Seymour)
        
    if checked == "n":
        Seymour.dragonAttack()
    else:
        checked = continueCare(Audrey, Seymour)

main()
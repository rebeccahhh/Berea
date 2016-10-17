# story.py
# simple story program created to demonstrate use of the Queue class

from queue import Queue

q=Queue() # global queue to hold story

def print_intro():
    '''This function prints the opening splash.'''
    print("WELCOME TO STORY BUILDER!\n")
    print("Each person adds one word (and accompanying punctuation) to the story.")
    print("\n Have fun!!!\n")
    print("When someone wishes to end the story, he or she types END in all caps.\n")
    return

def fix_input(entry):
    ''' this function handles user input by converting to integers'''
    try:
        val=int(entry)
        if val<0:
            val=0
    except ValueError:
        val=q.size()-1 # non-numeric input will result in the entire story being printed
    return(val)

def main():

    print_intro()
    s=raw_input("Please enter the first word of the story: ") # string to hold each word of story one at a time
    q.enqueue(s)
    while (s!="END"):
        s=raw_input("Please enter the next word of the story: ")
        q.enqueue(s)

    print("")
    entry=raw_input("How many words of the story would you like? (enter a number or 'all'): ")

    val=fix_input(entry)
    print("")
    print ("STORY:"),
    for i in range(val):
        print (q.dequeue()),

if __name__ == '__main__':
    main()

from binarynodes import binarynodes
import sys

class riddler():
    def __init__(self):
        self.root = binarynodes() 
        self.currentNode = binarynodes()
        #parent node
        # self.yorn = None #users answer
        # self.answer = None #correct answer
        # self.endit = None #state dependant??

    def read_recursion(self, inFile, currentNode):
        """First argument is the handle to the file being read, and
        the second is the current node.
        Pre: currentNode has been created already, and inFile refers to a
             valid file that has been opened for reading.
        Post: currentNode will either have no children if it is a guess
              or two children if it is a question. Either the guess or
              the question will be saved in its 'data' instance variable."""
        category = inFile.readline()
        
        # continue to read from the file, eating up white space. Note that
        # readline() includes the newline at the end of the line in the file.
        # hence the '\n' after each possible value for category.
        while category != "Guess:\n" and category != "Question:\n":
            category = inFile.readline()
        data = inFile.readline()
        currentNode.set_value( data )
        
        # check for base case. If we are not at a question, we are at the
        # guesses in the leaves.
        if category != "Question:\n":
            return
        
        # first create the necessary child and then pass it to the recursion
        currentNode.right = binarynodes()
        self.read_recursion( inFile, currentNode.right )
        currentNode.left = binarynodes()
        self.read_recursion( inFile, currentNode.left )
   
    
    def nananananananananaBATMAN(self):
        '''asks the user if they want to play'''
        
        self.yorn = raw_input("Would you like to play a game? y/n: ")
        if self.yorn.lower() == "yes" or self.yorn.lower() == "y":
            print ("Now the real game begins!")
            inFile = open('animalTree.txt', 'r')
            self.read_recursion(inFile, self.root)
            print ("Golly Galoshes Batman!")
            self.riddle_me_this_Batman(self.root)
        elif self.yorn.lower() == "no" or self.yorn.lower() == "n":
            print("Playing the long game eh?")
            sys.exit()
        else:
            print ("Secret Identity exposed!")
   
            
    def riddle_me_this_Batman(self, thisNode):
        #question platform
        user_input = raw_input(thisNode.value)
        if user_input == 'y':
            self.riddle_me_this_Batman(thisNode.right)
        elif user_input == 'n':
            self.riddle_me_this_Batman(thisNode.left)
        else:
            print("Quick Robin! To the Batmobile!")
        
        
        # question = raw_input(self.root.value)
        # if question.lower() == 'y' or question.lower() == 'yes':
        #     self.root = self.root.left
        # elif question.lower() == 'n' or question.lower() == 'no':
        #     self.root = self.root.right
        # else:
        #     print("Alfred I need you!")


                
   # def penguin(self):
        

    
    # def foiled(self, guess):
    #     #subtree insertion
    #     prompt  = "What is the animal's name?"
    #     animal  = raw_input(prompt)
    #     prompt  = "What question would distinguish a {0} from a {1}? "
    #     question = raw_input(prompt.format(animal, guess))

    #     # Add new information to the tree
    #     self.root.value = question
    #     prompt = "If the animal were {0} would the answer would be yes? "
    #     if prompt.format(animal) == "yes":
    #         self.root.left = binarynodes(guess)
    #         self.root.right = binarynodes(animal)
    #     else:
    #         self.root.left = binarynodes(animal)
    #         self.root.right = binarynodes(guess)
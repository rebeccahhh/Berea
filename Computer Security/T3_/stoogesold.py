def login():
    user = ()
    if user == "shemp":
        shemp()
    elif user == "curly":
        curly()
    elif user == "larry":
        larry()
    elif user == "moe":
        moe()
    else:
        print ("WHOOPWHOOPWHOOPWHOOPWHOOP! Ohhhh a wise guy, eh?")
     
 
def filehandler():
    #Mechanism to allow users of appropriate 
    print "handling files"
        
class shemp():
    def _init_(self):
        self.password = ""
        self.person = "shemp"
    def password_so_secret(self):
        if raw_input(("Welcome, enter your password:").lower()) == self.password:
            request = (raw_input("Do you want to read or write?").lower)
            if request == "read" or "r":
                #print shempfiles
                file = raw_input("which file do you want to use?")
                newfile = open(file, "r")
            elif request == "write" or "w":
                filehandler()
                file = raw_input("which file do you want to use?")
                newfile = open(file, "w")
            else:
                print "error boop beep boop, try again"
                request
        
class curly(shemp):
    def _init_(self):
        self.password = "string"
        self.person = "curly"
        
class larry(curly, shemp):
    def _init_(self):
        self.password = "more string"
        self.person = "larry"

class moe(larry, curly, shemp):
    def _init_(self):
        self.password = "most string"
        self.perons = "moe"


def Main():
    login()
Main()
import sys

class shemp():
    def __init__(self):
        self.password = ""
        self.person = "shemp"
        
    def read_permissions_checkself(self, author):
        if author == self.person:
            return True
            
    def write_permissions_checkself(self, author):
        return True
            
    def prompt_password(self):
        ''' prompts the user for their password '''
        input = raw_input("Welcome, " + self.person + ", enter your password: ").lower()
        if input != self.password:
            while input != self.password:
                print ("WHOOPWHOOPWHOOPWHOOPWHOOP! Ohhhh, a wise guy, eh? ")

    def file_prompt(self):
        ''' prompts the user to read or write a file '''
        input = (raw_input("Do you want to read, write, or create a file? ").lower())
        if input != "read" and input != "write" and input != "create":
            while input != "read" and input != "write" and input != "create":
                input = raw_input("WHOOPWHOOPWHOOPWHOOPWHOOP! Ohhhh, a wise guy, eh? ")
        if input == "read":
            self.read_file()
        elif input == "write":
            self.create_file()
        else:
            self.create_file()
            
    def create_file(self):
        ''' creates a file and labels it with the username '''
        file_name = raw_input("Enter the name of your file: ")
        try: #writes to an existing file
            new_file = open(file_name, "r")
            temp = new_file.readline().strip()
            if self.write_permissions_checkself(temp) == True:
                current = new_file.read()
                input = raw_input("Type what you want to write in the existing file here: ")
                new_file.close()
                new_file = open(file_name, "w")
                new_file.write(temp + current + "\n\n" + input)
                new_file.close()
            else:
                print "Sorry, this file is too plebian to write to."
                sys.exit()

        except IOError: #creates a file
            new_file = open(file_name, "w")
            new_file.write(self.person + "\n\n")
            input = raw_input("Type what you want to write in the new file here: ")
            new_file.write(input)
            new_file.close()  
        
    def get_file(self):
        ''' returns the user's input file's name as a str '''
        is_correct = False
        while not is_correct:
            try:
                input = raw_input("Type the name of your file please: ")
                new_file = open(input, "r")
                is_correct = True
            except IOError:
                print "WHOOPWHOOPWHOOPWHOOPWHOOP! Ohhhh, a wise guy, eh? "
        new_file.close()
        return input

    def read_file(self):
        ''' prints the contents of a file to the console '''
        new_file = open(self.get_file(), "r")
        if self.read_permissions_checkself(new_file.readline().strip()) == True:
            print new_file.read()
            new_file.close()
        else:
            print "Sorry, you can't read this file."
            sys.exit()

    def password_so_secret(self):
        ''' Handles user access and actions for files '''
        if self.person != "shemp":
            self.prompt_password()
        self.file_prompt()

class curly(shemp):
    def __init__(self):
        self.password = "string"
        self.person = "curly"

    def read_permissions_checkself(self, author):
        if author == self.person or author == "shemp":
            return True
            
    def write_permissions_checkself(self, author):
        if author == self.person or author == "moe" or author == "larry":
            return True
            
class larry(curly):
    def __init__(self):
        self.password = "more string"
        self.person = "larry"
        
    def read_permissions_checkself(self, author):
        if author == self.person or author == "shemp" or author == "curly":
            return True
            
    def write_permissions_checkself(self, author):
        if author == self.person or author == "moe":
            return True
            
class moe(larry):
    def __init__(self):
        self.password = "most string"
        self.person = "moe"
    
    def read_permissions_checkself(self, author):
        return True
            
    def write_permissions_checkself(self, author):
        if author == self.person:
            return True

def get_user():
    ''' returns the user's username as an object'''
    current_user = raw_input("Enter your username: ").lower()
    if current_user != "curly" and current_user != "shemp" and current_user != "moe" and current_user != "larry":
        while current_user != "curly" and current_user != "shemp" and current_user != "moe" and current_user != "larry":
            current_user = raw_input("WHOOPWHOOPWHOOPWHOOPWHOOP! Ohhhh, a wise guy, eh? ")
    if current_user == "shemp":
        return shemp()
    elif current_user == "curly":
        return curly()
    elif current_user == "larry":
        return larry()
    elif current_user == "moe":
        return moe()

def Main():
    user = get_user()
    user.password_so_secret()

Main()


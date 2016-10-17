# ask the user for a filename from which it will take its input
# open the file with that filename and reads an integer at the beginning of the file that is the number of lines that follow
# open a file called output.txt
# reads in the strings of the input, one at a time, and writes to the output file either "accept" or "reject" 
#   depending on whether the program is in error state at the end of each string
# closes both files

class file():
    def read_letters(self, file):
        self.state = 1
        num = file.readline().strip()
        num_of_lines = int(num)
        print num_of_lines
   
    #While there are still lines to be read, read each letter in each line and 
    #correlate it to a state.
        while num_of_lines != 0:
            nextline = file.readline().strip()
            print nextline
            for x in nextline:
                if self.state == 1:
                    if x.isalpha():
                        self.state = 3
                    elif x.isdigit():
                        self.state = 2
                    else:
                        error()
                elif self.state == 2:
                    if x.isalpha():
                        self.state = 2
                    elif x.isdigit():
                        self.state = 2
                    else:
                        error()
                elif self.state == 3:
                    if x.isalpha() or x.isdigit():
                        self.state = 3
                    else:
                        error()
            num_of_lines = num_of_lines - 1
            
        #If all the lines have been read, open a file and write the final 
        #accept or reject state to the file.
        if num_of_lines == 0:
            if self.state == 3:
                print "Accept"
                out = open("output.txt", "w")
                out.write("Accept")
            elif self.state == 2 or self.state == 1:
                print "Reject"
                out = open("output.txt", "w")
                out.write("Reject")
            else:
                print "Final State Error"
                
def error():
    print "Error, program will exit until the programmer gets her life together."

def main():
    #works when providing a file, not when obtaining file name from user though
    #FIX THIS
    #file = raw_input("Please enter the filename:")
    #if file == "input.txt" or file == "anotherinput.txt":
    #    name = open(file, "r")
    #    file().read_letters(name)
    #else:
    #    print "oops, try again."
        
##################################
#   I struggled to implement the input section, which logically seems right, 
#   but I'm struggling with syntax. I will try to fix, however, the state
#   logic is correct, and can be tested by commenting and uncommmenting
#   each of these 3 individual files provided below.
##################################
    #name = open("input.txt", "r")          #Accept
    #name = open("anotherinput.txt", "r")   #Accept
    name = open("lastinput.txt", "r")       #Reject
    file().read_letters(name)   
main()
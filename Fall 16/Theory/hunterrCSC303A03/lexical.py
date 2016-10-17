# 1. ask the user for a filename from which it will take its input
# 2. ask the user for a filename from which it will create the transition table.
# 3. open the file with the table information, in which 
#       a. the first two numbers are the number of rows (number of states), and the number of columns (number of symbols).
#       b. next, there will be a list of symbols, the number of which corresponds to the second number read above minus one (the EOS is not a symbol in the alphabet)
#       c. next, there will be the information to make a table, either using 2D arrays in C++ or a list of lists in Python
#           For example, the transition table on page 25 would have a file that can look like:
#               3 3
#               letter, digit
#               3 2 error error error error 3 3 accept
# 4. use the (current_state, symbol) combination to figure out which state it will enter as a result using this table. Note that instead of Input:="letter" in the analyzer on page 25, you can set Input to the column index.
# 5. open the file with that filename and reads an integer at the beginning of the file that is the number of lines that follow
# 6. open a file called output.txt
# 7. reads in the strings of the input, one at a time, and writes to the output file either "accept" or "reject" depending on whether the program is in error state at the end of each string
# 8. closes both files

def lexical_analysis(input_symbols, state):
    #to analyze the inputs after they've been converted to just letter or digit
    if input_symbols[0] == "letter":
    #if the first symbol is a letter, continue, if not, an accept state cannot be achieved.
        state = 3
        for x in input_symbols:
            if x == "letter":
                state = 3
            elif x == "digit":
                state = 3
            elif x == "EOS":
                state = "accept"
                print "accepted"
            else:
                print "error"
    elif input_symbols[0] == "digit":
        state = 2
        print "digit, error state"
    else:
        print "first symbol error"
    

    
def converter(input_file):
    input_symbols = []
    lines = input_file.readlines()
    print lines
    for x in lines:
        print x
        if x.isalpha: 
            input_symbols.append("letter")
        elif x is int:
            input_symbols.append("digit")
        elif x == "/n":
            input_symbols.append("EOS")
        else:
            "conversion error"
    return input_symbols
    
def main():
    state = 1
    input_filename = raw_input("enter input filename:")
    input_file = open(input_filename, "r")
    line = input_file.readlines()
    symbols = line.split()
    print input_file
    #table_file = raw_input("enter transition table filename:")
    symbols = converter(symbols)
    #print "symbol success"
    lexical_analysis(symbols, state)
    #print "lexical success"
    
main()
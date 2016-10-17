# parensBalance2.py
#
# modified from code by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

# modifications:
#   * added functionality to ignore all other characters so expressions could be checked.
#   * added the main function and the main function call
#   * added numerous print statements to make function verbose

from Stack import Stack

def parensBalance2(s):
    stack = Stack()
    for ch in s:
        if ch in "(){}[]": #ignores characters others than parentheses
            if ch in "([{":      # push an opening marker
                stack.push(ch)
            elif ch in ")]}":    # match closing with top of stack
                if stack.size() < 1: # no pending open to match it
                    print("No opening bracket to match " + ch)
                    return False
                else:
                    opener = stack.pop()
                    if opener+ch in ["()", "[]", "{}"]:
                        print(opener+ch)
                    else:
                       # not a matching pair
                       print("Tried to match " + opener + " with " + ch)
                       return False
    print ("stack size is "+str(stack.size()))
    return stack.size() == 0 # an empty stack means everything matched up

def main():
    print("")
    seq=raw_input("Please enter an arithmetic sequence for parentheses checking: ")
    is_matched=parensBalance2(seq)
    if int(is_matched):
        print(seq + " is well-matched.")
    else:
        print(seq + " is NOT well-matched.")

if __name__ == '__main__':
    main()

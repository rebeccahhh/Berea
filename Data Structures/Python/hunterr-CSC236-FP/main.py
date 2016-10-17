#------------------------------------------------------------------------------#
# Name:     Rebeccah Hunter  
# File:     main.py
# Purpose:  The goal of this program is to expand upon the manipulation and analysis of data
#   structures in A3 and A16 that was covered in CSC 236 taught by Mario Nakazawa in the
#   fall semester of 2015 at Berea College.
#   Acknowledgements to the Berea College Computer Science staff, particularly
#   Mario Nakazawa, as well as the BC CS TA's.
#
# Collaborates with: sorting.py, Node.py, search.py, BinaryTree.py, and input files.
#------------------------------------------------------------------------------#
import sys
import time
from Node import Node
from search import search
from BinaryTree import BinaryTree
from sorting import sorting

def main():
    """
    This program akes an input file and sorts the file, counting the 
    occurances of a word and eliminates the extra occurances so there is just
    one instance of the word into an ordered list at which point it will
    create a binary tree based on the information with each node containint the
    item, the number of times the item occurred in the text document, as well
    as the right and left children. It will then search the binary tree.
    """
#-------------------- opens text and sorts it into nested list ---------------#
    searching = search()
    #file_input = raw_input("Enter the name of your .txt file here: ")
    #file_input = 'FPinput.txt'  #For ease of testing
    file_input = 'longer_input.txt'
    sort_of = sorting()
    well = sort_of.read_words(file_input) # for ease of testing
    #looking_for = raw_input("Enter the word you are looking for here: ")
    looking_for = 'input' #test word
#-----------------------------------------------------------------------------#
    
    
#------- Performs a linear search and times it before the file is sorted -----#
    print("--------------------------------------------------")
    print ("The Linear Search will begin.")
    startLinear = time.time()
    searching.linear_search(looking_for, well)
    endLinear = time.time()
    timedLinear = endLinear - startLinear
    print ("Your time for the Linear search was:")
    print timedLinear
    print("--------------------------------------------------")
#-----------------------------------------------------------------------------#    

#-------------- Performs a binary search on the array and times it ------------#
    print ("The Binary Search will begin.")
    startBinary = time.time()
    searching.binary_search(looking_for, well)
    endBinary = time.time()
    timedBinary = endBinary - startBinary
    print ("Your time for the Binary search was:")
    print timedBinary
    print("--------------------------------------------------")
#-----------------------------------------------------------------------------#    
    

#---------------------- creates binary tree ----------------------------------#
    print("The following words have been sorted and counted, as indicated by the number beside them.")
    file_array = sort_of.count_words(well)
    print("--------------------------------------------------")
    run = Node()
    run_forrest = BinaryTree()
    run.set_value(file_array[(len(file_array)/2)])
    print ("The following values have been populated into a Binary Tree.")
    running = run_forrest.populate_from_array(run, file_array, len(file_array))
    running
    print("--------------------------------------------------")
#-----------------------------------------------------------------------------#   
    

#-------------- Performs a binary search on the tree and times it ------------#
    print ("The Binary Tree Search will begin.")
    startBinaryST = time.time()
    run_forrest.binary_searchT(looking_for, run)
    endBinaryST = time.time()
    timedBinaryST = endBinaryST - startBinaryST
    print ("Your time for the Binary search was:")
    print timedBinaryST
    print("--------------------------------------------------")
#-----------------------------------------------------------------------------#    
        

    
main()
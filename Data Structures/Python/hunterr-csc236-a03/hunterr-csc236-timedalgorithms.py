################################################################################
# Name: Search Comparison Generator
#   Purpose: to read given .txt files and calculate the difference in 2
#       different search techinques (binary and linear).
# Author: Rebeccah Hunter
# Acknowledgements: Berea College Computer Science, Dr. Nario Nakazawa.
################################################################################
import time
import sys

#test_list = ['a', 'a','a', 'a','a', 'a','a', 'a','a', 'a','b']

def read_words(words_file_name):
## This function is adapted from
##  http://stackoverflow.com/questions/13259288/returning-a-list-of-words-after-reading-a-file-in-python
## with exception handling built into it. Also integrated is a method to
## strip punctuation usingideas/code from
##      http://stackoverflow.com/questions/19414161/removing-punctuation-in-lists-in-python
    '''This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail. '''
    words_list = []
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readlines()

        # replace punctuation with a blank space
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        for i in punctuation:
            for j in range(len(contents)):
                contents[j] = contents[j].replace(i,"")

        for i in range(len(contents)):
            contents[i].lower()
            words_list.extend((contents[i].lower()).split())
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    return words_list

def binary_search(itemSought, input_list):
    '''This function should utilse binary search to locate and count the number
    of the user's desired word.'''
    first = 0
    final = len(input_list)
    found = False
    count = 0
    while first <= final and found == False:
        middle = (first + final)//2
        while input_list[middle] == itemSought:
            count + 1
            found = True
            print count
            #print "test for infinite loop"
        if input_list[middle] > itemSought:
            first + 1
            found = False
            #print "test again"
        elif input_list[middle] < itemSought:
            final - 1
            found = False
        else:
            print "There has been an error."
            break
        

def linear_search(itemSought, input_list):
    '''counts the number of items in a user provided file that was converted to
    list using read_words()'''
    countSought = input_list.count(itemSought)
    print countSought
    return countSought

def main():
    input_list = raw_input("Please enter the name of the desired text file: ")
    itemSought = raw_input("Please choose a single word to count without spaces: ")
    startLinear = time.time()
    linear_search(itemSought, read_words(input_list))
    endLinear = time.time()
    timedLinear = endLinear - startLinear
    print ("Your time for the Linear search was:")
    print timedLinear
    startBinary = time.time()
    binary_search(itemSought, read_words(input_list))
    endBinary = time.time()
    timedBinary = endBinary - startBinary
    print ("your time for the Binary Search was: ")
    print timedBinary

main()
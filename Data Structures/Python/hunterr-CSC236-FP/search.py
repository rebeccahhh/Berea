#------------------------------------------------------------------------------#
# Name:     Rebeccah Hunter  
# File:     search.py
# Purpose:  To search a given array and be utilised in main.py
#
#   Will be timed in main.py. Iterates through each list in either a
#   linear or binary fasion.
#
#------------------------------------------------------------------------------#
import time
import sys

class search:  
    """
    A class designed to allow the user to search a given array both in a linear
    and a binary fasion.
    """

    def __init__(self):
        self.stuff = ''
        
    def binary_search(self, itemSought, input_list):
        '''utilises binary search and counts the number of items in a user 
        provided file that was converted to an array using read_words()'''
    #--------------------------------------------------------------------------#
    #------Sets up the variables to be used within the while statment----------#
    #--------------------------------------------------------------------------#
        final = len(input_list)
        first = 0
        count = 0
        found = False
        
    #--------------------------------------------------------------------------#
    #----------While the value is not found, execute the following-------------#
    #--------------------------------------------------------------------------#
        while first <= final and found is False:
            middle = (first + final)//2
            itemFound = input_list[middle]
            if itemFound == itemSought:
                count = count + 1
                found = True
                print ("the Binary Search found ") + str(count) + (" instances of your word.")
                return itemSought
            elif itemFound >= itemSought:
                first = first + 1
                found = False
                # print itemFound + " >="       #Error found with Binary Search, transitioning it into a class has changed it somehow, and it is no longer working.
            elif itemFound <= itemSought:
                final = final - 1
                found = False
                # print itemFound + " <="       #Error is that search seems to never reach desired base case to count occurances.
            else:
                found = True
                print "There has been an error."
        return itemSought       
                
              
                
    def linear_search(self, itemSought, input_list):
        '''does a linear search and counts the number of sought items in a user 
        provided file that was converted to array using read_words()'''
        countSought = input_list.count(itemSought)
        return countSought
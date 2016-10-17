#------------------------------------------------------------------------------#
# Name:     Rebeccah Hunter  
# File:     Node.py
# Purpose:  A Node class for use in a binary tree
#------------------------------------------------------------------------------#
class Node():
    #--------------------------------------------------------------------------#
    #------A simple node class with a small addition to include more ----------#
    #------information, which is stored in the same way that value is.---------#
    #--------------------------------------------------------------------------#
    def __init__(self):
        self.count = 0
        self.data = ''
        self.right = None
        self.left = None

    def set_value(self, value):
        ''' Sets the word value to the node. '''
        self.data = value
        
    def set_count(self, count):
        ''' Updates the word count in the node. '''
        self.count = count

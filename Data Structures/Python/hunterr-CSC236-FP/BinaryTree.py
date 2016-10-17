#------------------------------------------------------------------------------#
# Name:     Rebeccah Hunter  
# File:     BinarySearchTree.py
# Purpose:  CSC 236 Example of creating and using binary search trees in Python.
#
#   Shows how to use a tree to store information, and in particular how to
#   search through a binary search tree. This program both creates a binary
#   search tree given an array, searches the tree given a target value, and
#   deletes the tree before the program ends.
#
#------------------------------------------------------------------------------#
import sys
from Node import Node

class BinaryTree():
    """
    A class created with a method to create a binary tree, and another to search
    the binary tree after it's created.
    """
    def __init__(self):
        self.node = Node()
        
    def populate_from_array(self, current_node, given_array, arraySize):
        """
        Takes a current node, an array, and the array size and creates a binary tree.
        This section of code was my single biggest issue in creating this program.
        """
        #--------------------------------------------------------------------------#
        #-------------This section of code is originally from A16------------------#
        #--------------------------------------------------------------------------#
        if current_node == None:
            return ("")
        if current_node.left != None:
            print('error' and current_node.left)
        if current_node.right != None:
            print("error" and current_node.right)
        if arraySize == 1:
            return arraySize
    
        new_node = Node()
        new_node.set_value(current_node.left)
        new_node.set_count(current_node.left)
        left_array = []
        for i in range(arraySize/2):
            left_array.append(given_array[i])
            print(str(given_array[i]))

        self.populate_from_array(current_node.left, left_array, arraySize)
        del left_array[:]
        right_size = arraySize/2 + 1
        #print right_size
        if right_size == 0:
            return arraySize
    
        newer_node = Node()
        newer_node.set_value(current_node.right)
        new_node.set_count(current_node.left)
        right_array = []
        for i in range(right_size):
            right_array.append(given_array[(right_size/2)+i])
            print(str(right_array[i]))
            
        self.populate_from_array(current_node.right, right_array, arraySize)
        del right_array[:]
        left_size = arraySize/2 - 1
        #print left_size
        if left_size == 0:
            return arraySize
        return current_node
            
            
            
    def binary_searchT(self, itemSought, current_node):
        """
        A brief search through a binary tree.
        """
        if itemSought < current_node:
            if current_node.left is None:
                return None, None
            return current_node.left
        elif itemSought > current_node:
            if current_node.right is None:
                return None, None
            return current_node.right
        else:
            return current_node

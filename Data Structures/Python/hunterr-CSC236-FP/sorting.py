#------------------------------------------------------------------------------#
# Name:     Rebeccah Hunter  
# File:     sorting.py
# Purpose:  Takes a given file and can read from file or sort words from array
#
#   read_words takes a given file, opens it, removes all punctuation and
#   capitalization.
#   count_words takes the array that was populated from read_words and counts
#   the instances of the specified word.
#
#------------------------------------------------------------------------------#
from collections import Counter

class sorting:
    def __init__(self):
        self.final_list = []
        self.intermediate_list = []
    
    def read_words(self, words_file_name):
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
                    
            # makes all words lower case
            for i in range(len(contents)):
                contents[i].lower()
                words_list.extend((contents[i].lower()).split())
            open_file.close()
        except IOError:
            print("File does not exist! Please try again.")
        return words_list
        
    def count_words(self, words_list):
        """An addition to the program that counts the words in a sorted array
        in a fashion much like a dictionary, with 'keys' and 'values', 
        the keys being the words that were counted, and the values being the 
        number of occurances of that word. The extra words are then deleted."""
        
        sorted_list = sorted(words_list)
        cou = Counter(sorted_list)
        #----------------------------------------------------------------------#
        #-------The following were for testing during early development--------#
        #----------------------------------------------------------------------#
        #print str(cou)
        #self.number_of_words.append(cou.values())
        #print cou.values()
        #self.counted_word.append(cou.keys())
        #print str(cou.keys())
        #----------------------------------------------------------------------#
        #----------------------------------------------------------------------#
        
        x = 0
        for i in cou.keys():
            #For loop that creates a new list of all the keys and values in order
            #i.e. [word, #, word, #, word, #, word, #,...etc]
            self.intermediate_list.append(i)
            self.intermediate_list.append(cou.values()[x])
            x = x+1
        #print(self.intermediate_list) #for testing during development
        
        x = 0
        for i in cou.keys():
            #for loop that utilises splicing to create nested lists in this
            #format: [[word, #], [word, #],...etc.]
            self.final_list.append(self.intermediate_list[x:x+2])
            x = x+2
        #print(self.final_list) #for testing during development
        
        return self.final_list
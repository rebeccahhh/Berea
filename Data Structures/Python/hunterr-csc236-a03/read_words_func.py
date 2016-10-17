#-------------------------------------------------------------------------------
# Name:        read_words_function.py
# Purpose:  This sample function opens a file with the name words_file_name
#   reads the text, converts everything to lowercase and returns a list
#   of the words.
#
# Author:       various online sources cited in the comment above function
#
# Created:     25/08/2014
#-------------------------------------------------------------------------------

## This function is adapted from
##  http://stackoverflow.com/questions/13259288/returning-a-list-of-words-after-reading-a-file-in-python
## with exception handling built into it. Also integrated is a method to
## strip punctuation usingideas/code from
##      http://stackoverflow.com/questions/19414161/removing-punctuation-in-lists-in-python
def read_words(words_file_name):
    '''This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail. '''
    words_list =[]
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

def main():
    input_words = read_words("gettysburg.txt")
    print(input_words)

if __name__ == '__main__':
    main()
    
    
    
    
    # def binary_search(itemSought, input_list):
    #     itemFound = False
    # while itemFound == False
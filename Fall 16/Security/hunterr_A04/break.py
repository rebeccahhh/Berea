#------------------------------------------------------------------------------#
# Computer Security - Dr. Scott Heggen
# Author - Rebeccah Hunter
# Thanks to the snazzy Austin Farmer
#------------------------------------------------------------------------------#

import math

def decrypt(inputCipher):
    print "The length of the string is: ", len(inputCipher)
    rootValue = int(math.sqrt(len(inputCipher)))
    print "The matrix is ", rootValue, "x", rootValue
    test = ""
    for x in range(rootValue):
        for y in range(rootValue):
            test += (inputCipher[rootValue * y + x])
            output = file("output.txt", "w")
            output.write(test)
    print test
  
def main():
    #cipherText = file("A4_cipher_small.txt", "r")
    cipherText = file("A4_cipher_large.txt", "r")
    decrypt(cipherText.read())
main()
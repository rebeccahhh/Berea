__author__ = 'heggens'
'''
This program implements three encryption algorithms:
Simple cipher, stream cipher, and a block cipher
'''

# Implementing a Simple Cipher (ceasar cipher style)
def encryptSimpleCipher(plainText, key):
# Encrypts a file using a simple cipher, then writes it to a file.
    output = ""
    print key
    for x in plainText:
        print ("The ASCII value of "+ str(x.lower()) + " is " + str(ord(x.lower())))
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            output = output + key[ord(x.lower()) - 97]
            print output
        else:
            output = output + x
    newfile = open("cipher.txt", "w")
    newfile.write(output)
    # TODO encrypt the simple cipher. Save the output to a new file and return it to the calling function.
    return output

def decryptSimpleCipher(cipherText, key):
        print ("CUrr")
    for x in cipherText:
        print ("The ASCII value of "+ str(x.lower()) + " is " + str(ord(x.lower())))
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            output = output + key[ord(x.lower()) - 103]
            print output
        else:
            output = output + x
    # newfile = open("cipher.txt", "w")
    # newfile.write(output)
    print output
    return output
    
def decryptMonoCipher(cipherText, key):
    output = ""
    
    for x in cipherText:
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            
            print output
        else:
            output = output + x
    # newfile = open("cipher.txt", "w")
    # newfile.write(output)
    print output
    return output

# Implementing Stream Cipher
def encryptStreamCipher(plainText, key):
    output = ""
    # TODO encrypt the stream cipher. Save the output to a new file and return it to the calling function.
    return output

def decryptStreamCipher(cipherText, key):
    output = ""
    # TODO decrypt the stream cipher. Save the output to a new file and return it to the calling function.
    return output


# Implementing Block Cipher
def encryptBlockCipher(plaintext, key):
    output = ""
    # TODO encrypt the block cipher. Save the output to a new file and return it to the calling function.
    return output

def decryptBlockCipher(cipherText, key):
    output = ""
    # TODO decrypt the block cipher. Save the output to a new file and return it to the calling function.
    return output


def main():
    key = open('monokey.txt').read()

    plainText = open('plain.txt', 'r').read()
    outputCipher = encryptSimpleCipher(plainText, key)
    print outputCipher
    
    # cipherText = open('cipher.txt', 'r').read()    
    # inputCipher = decryptSimpleCipher(cipherText, key)
    # print inputCipher
    
    monoCipherText = open('cipher.txt', 'r').read()    
    inputCipher = decryptMonoCipher(monoCipherText, key)
    print inputCipher
    # outputCipher = encryptStreamCipher(plainText, key)
    # outputCipher = encryptBlockCipher(plainText, key)
    # print "The encrypted message is: {}".format(outputCipher)

    # ########################################################################

    # # Now, we'll assume we are the receiver, and want to decrypt the message
    # outputPlain = decryptSimpleCipher(outputCipher, key)
    # # outputPlain = decryptStreamCipher(outputCipher, key)
    # # outputPlain = decryptBlockCipher(outputCipher, key)
    # print "The received message is: ".format(outputPlain)


main()

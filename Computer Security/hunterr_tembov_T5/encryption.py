__authors__ = 'tembov', 'hunterr'
'''
This program implements three encryption algorithms:
Simple cipher, stream cipher, and a block cipher.
'''
from math import ceil
#------------------------------------------------------------------------------#
#-------------Implementing a Simple Cipher (ceasar cipher style)---------------#
#------------------------------------------------------------------------------#
def encryptSimpleCipher(plainText, key):
# Encrypts a file using a simple cipher, then writes it to a file.
    output = ""
    for x in plainText:
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            output = output + key[ord(x.lower()) - 97]
            #print output
        else:
            output = output + x
    newfile = open("cipher.txt", "w")
    newfile.write(output)
    newfile.close()
    return output

def decryptSimpleCipher(cipherText, key):
# decrypts a file using a simple cipher, then writes it to a file.
    output = ""
    for x in cipherText:
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            output = output + key[ord(x.lower()) - 103]
        else:
            output = output + x
    newfile = open("plain.txt", "w")
    newfile.write(output)
    newfile.close()
    return output
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#

    

#------------------------------------------------------------------------------#
#-----------------------Implementing Monoalphabetic cipher---------------------#
#------------------------------------------------------------------------------#    
def encryptMonoCipher(plainText, key):
# Encrypts a file using a simple cipher, then writes it to a file.
    output = ""
    for x in plainText:
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            output = output + key[ord(x.lower()) - 97]
        else:
            output = output + x
    newfile = open("monocipher.txt", "w")
    newfile.write(output)
    newfile.close()
    return output
    
def decryptMonoCipher(cipherText, key):
    output = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in cipherText:
        if ord(x.lower()) > 96 and ord(x.lower()) < 123:
            output = output + alpha[key.find(x)]
            #print output
        else:
            output = output + x
    newfile = open("plain.txt", "w")
    newfile.write(output)
    newfile.close()
    return output
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#




#------------------------------------------------------------------------------#
#----------------------Implementing Stream Cipher------------------------------#
#------------------------------------------------------------------------------#
def encryptStreamCipher(plainText, key):
    output = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newkey = key*int(ceil(float(len(plainText))/float(len(key))))
    newkey = newkey[:len(plainText)-1]
    for x in range(len(newkey)):
        if ord(plainText[x].lower()) > 96 and ord(plainText[x].lower()) < 123:
            numx = alpha.find(plainText[x].upper()) 
            nums = alpha.find(newkey[x].upper())
            numf = (nums + numx)%26
            output = output + alpha[numf]
        else:
            output = output + plainText[x]
    encryptstream = open('streamencrypted.txt', 'w')
    encryptstream.write(output)
    encryptstream.close()
    return output


def decryptStreamCipher(cipherText, key):
     output = ""
     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     newkey = key*int(ceil(float(len(cipherText))/float(len(key))))
     newkey = newkey[:len(cipherText)]
     for x in range(len(newkey)):
         if ord(cipherText[x].lower()) > 96 and ord(cipherText[x].lower()) < 123:
             cipher_num = alpha.find(cipherText[x].upper()) 
             key_num = alpha.find(newkey[x].upper())
             final_num = (cipher_num%26) - key_num
             output = output + alpha[final_num]
         else:
             output = output + cipherText[x]
     decryptstream = open('streamdecrypted.txt', 'w')
     decryptstream.write(output)
     decryptstream.close()
     return output
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
#------------------------Implementing Block Cipher-----------------------------#
#------------------------------------------------------------------------------#
# def encryptBlockCipher(plaintext, key):
#     output = ""
#     # TODO encrypt the block cipher. Save the output to a new file and return it to the calling function.
#     return output

# def decryptBlockCipher(cipherText, key):
#     output = ""
#     # TODO decrypt the block cipher. Save the output to a new file and return it to the calling function.
#     return output
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#




#------------------------------------------------------------------------------#
#------------------------------Main Function-----------------------------------#
#------------------------------------------------------------------------------#
def main():
#---------------------------Simple Cipher--------------------------------------#
    simplekey = open('key.txt').read()
    plainText = open('plain.txt', 'r').read()
#encryption
    outputCipher = encryptSimpleCipher(plainText, simplekey)
#decryption
    cipherText = open('cipher.txt', 'r').read()    
    inputCipher = decryptSimpleCipher(cipherText, simplekey)
#------------------------------------------------------------------------------#



#--------------------Monoalphabetic substitution cipher------------------------#
    monokey = open('monokey.txt').read()
    plainText = open('plain.txt', 'r').read()
#encryption - same as simple above.
    outputCipher = encryptMonoCipher(plainText, monokey)
#Monoalphabetic Substitution Cipher Decryption - (Encryption is the same as the simple cipher)
    monoCipherText = open('monocipher.txt', 'r').read()
    inputCipher = decryptMonoCipher(monoCipherText, monokey)
#------------------------------------------------------------------------------#



#---------------------------Stream Cipher--------------------------------------#    
    longText = open('plainLong.txt', 'r').read()    
    streamkey = open('streamkey.txt').read()
#encryption
    outputCipher = encryptStreamCipher(longText, streamkey)
    #print "The encrypted message is: {}".format(outputCipher)
#decryption
    outputPlain = decryptStreamCipher(outputCipher, streamkey)
    #print "The decrypted message is: {}".format(outputPlain)
#------------------------------------------------------------------------------#


main()
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
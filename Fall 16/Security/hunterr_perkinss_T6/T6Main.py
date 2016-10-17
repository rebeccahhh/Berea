__author__ = 'heggens'

from Crypto.Cipher import DES, DES3
from Crypto import Random

KEY = "The key!"

iv = Random.new().read(DES3.block_size)
KEY2 = Random.new().read(DES3.key_size[-1])


def encryptDES(msg):
    encryption = DES.new(KEY)
    cipher = encryption.encrypt(msg)
    return cipher
    

def decryptDES(cipher):
    decryption = DES.new(KEY)
    plainOut = decryption.decrypt(cipher)
    return plainOut


def encrypt3DES(msg):
    enc = DES3.new(KEY2, DES3.MODE_ECB, iv)
    cipher = enc.encrypt(msg)
    return cipher


def decrypt3DES(cipher):
    dec = DES3.new(KEY2, DES3.MODE_ECB, iv)
    plainOut = dec.decrypt(cipher)
    return plainOut

def check_len(message):
    remain = len(message)%8
    if remain == 0:
        return message
    else:
        for x in range(remain):
            message += "x"
            return message

def main():
    message = "Hi class that is longer than the other messages\n"
    message_yes = check_len(message)
    cipher = encryptDES(message_yes)
    print "DES Cipher: " + str(cipher) + "\n"
    print "Back to message: " + decryptDES(cipher) + "\n"

    cipher = encrypt3DES(message_yes)
    print "DES3 cipher: " + cipher + "\n"
    print "Back to message: " + decrypt3DES(cipher)

main()
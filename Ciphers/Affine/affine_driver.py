"""
Program Name: Affine Cipher
Author: Blayne Wesneski
Date: August 31st, 2023
Description: This program allows the user to either encrypt or decrypt text using an affine cipher.
"""
from encrypt import encrypt
from decrypt import *

def affine():
    # Get the desired function from the user
    function = input("""
                    Please input the function you want to perform.
                    (1). Encrypt
                    (2.) Decrypt
                    """)

    if function == "1":
        # Encrypt the provided plaintext
        plaintext = input("What is the text you would like to encrypt? ")
        a = int(input("Please input the first key. "))
        b = int(input("Please input the second key. "))

        encrypt(plaintext, a, b)

    elif function == "2":
        # Decrypt the provided ciphertext
        ciphertext = input("What is the text you would like to decrypt? ")
        a = int(input("Please input the first key. "))
        b = int(input("Please input the second key. "))

        decrypt(ciphertext, a, b)
        
    else:
        exit()
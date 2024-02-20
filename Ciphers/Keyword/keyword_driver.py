# Author: Blayne Wesneski
# Date: 09/12/23
# Description: This script allows the user to either encrypt or decrypt text using a keyword cipher.

# Import the encrypt and decrypt functions from separate modules
from encrypt import encrypt
from decrypt import decrypt

# Prompt the user to choose between encryption (e) or decryption (d)
function = input("Would you like to encrypt or decrypt? (e/d) ")

if function == "e":
    # If the user chooses encryption, prompt for plaintext and keyword
    plaintext = input("Enter the text you would like to encrypt: ")
    keyword = input("Enter the keyword you would like to use: ")
    # Call encrypt() from encrypt.py
    encrypt(plaintext, keyword)

elif function == "d":
    # If the user chooses decryption, prompt for ciphertext and keyword
    ciphertext = input("Enter the text you would like to decrypt: ")
    keyword = input("Enter the key you would like to use: ")
    # Call decrypt() from decrypt.py
    decrypt(ciphertext, keyword)

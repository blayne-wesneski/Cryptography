"""
Program Name: Vigenere Cipher
Author: Blayne Wesneski
Date: October 2, 2023
Description: This program allows the user to encrypt and decrypt messages using a vigenere cipher.
"""

# Import the encrypt and decrypt functions from separate modules
from encrypt import encrypt
from decrypt import decrypt

# Prompt the user to choose between encryption (e) or decryption (d)
type = input("Would you like to encrypt or decrypt? (e/d): ")

# Check the user's choice
if type == "e":
    # If the user chooses encryption, prompt for plaintext and key
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    encrypt(plaintext, key)  # Call the encrypt function

elif type == "d":
    # If the user chooses decryption, prompt for ciphertext and key
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    decrypt(ciphertext, key)  # Call the decrypt function

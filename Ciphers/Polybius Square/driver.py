"""
Program Name: Polybius Square Cipher
Author: Blayne Wesneski
Date: September 20, 2023
Description: This program allows the user to encrypt and decrypt messages using a modified polybius cipher.
"""

# Import necessary functions and modules
from encrypt import encrypt
from decrypt import decrypt
from square import create_square
from apply_key import apply_key_enc, apply_key_dec

# Prompt the user to choose between encryption (e) and decryption (d)
type = input("What would you like to do? (e)ncrypt/(d)ecrypt): ")

# Encryption
if type == "e":
    # Input plaintext to be encrypted
    plaintext = input("What is the plaintext? ")

    # Input the encryption keys (key2 and key1)
    # Note: The keys are input in this order due to a later code issue
    key2 = input("What is the first key? ")
    key1 = input("What is the second key? ")

    # Create the encryption square
    square = create_square()

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, square)

    # Apply the encryption keys to the ciphertext
    ciphertext = apply_key_enc(ciphertext, key1, key2)

    # Display the ciphertext
    print("The ciphertext is: " + ciphertext)

# Decryption
elif type == "d":
    # Input the ciphertext to be decrypted
    ciphertext = input("What is the ciphertext? ")

    # Input the decryption keys (key2 and key1)
    # Note: The keys are input in this order due to a later code issue
    key2 = input("What is the first key? ")
    key1 = input("What is the second key? ")

    # Apply the decryption keys to the ciphertext
    ciphertext = apply_key_dec(ciphertext, key1, key2)

    # Create the encryption square
    square = create_square()

    # Decrypt the ciphertext
    plaintext = decrypt(ciphertext, square)

    print("The plaintext is: " + plaintext)
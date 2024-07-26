"""
Program Name: Ciphers
Author: Blayne Wesneski
Date: February 20th, 2024
Description: This program is a culmination of all the cipher programs I have written for my Cryptography class.
             It is made in order to cut down on the amount of Github Repos I have to manage.
             it allows the user to choose which cipher they would like to use and then encrypt or decrypt a message.
             It also contains the ability to conduct a frequency analysis on a given ciphertext.
"""

from encrypt import *
from decrypt import *
from analysis import analyze
from crack import crack_caeser
from square import create_square
from apply_key import apply_key_enc, apply_key_dec
from quick_modulo import logic


# Main function
def main():
    function = input(
        """What would you like to do?
                     (1) Encrypt a message with a cipher?
                     (2) Decrypt a message with a cipher?
                     (3) Conduct a frequency analysis on a ciphertext?
                     (4) Run the equation P = (x - y) mod 26 given 2 letters?
                     """
    )
    match function:
        case "1":
            encrypt()
        case "2":
            decrypt()
        case "3":
            frequency_analysis()
        case "4":
            quick_modulo()
        case _:
            print("Invalid input. Exiting.")
            exit()


# Choose encrytion cipher
def encrypt():
    cipher_choice = input(
        """What cipher would you like to encrypt with?
                     (1) Affine
                     (2) Caesar
                     (3) Keyword
                     (4) Polybius Square
                     (5) Vigenere
                     """
    )
    match cipher_choice:
        case "1":
            encrypt_affine()
        case "2":
            encrypt_caesar()
        case "3":
            encrypt_keyword()
        case "4":
            encrypt_polybius()
        case "5":
            encrypt_vigenere()
        case _:
            print("Invalid input. Exiting.")
            exit()


# Choose decryption cipher
def decrypt():
    cipher_choice = input(
        """What cipher would you like to decrypt with?
                     (1) Affine
                     (2) Caesar
                     (3) Keyword
                     (4) Polybius Square
                     (5) Vigenere
                     """
    )
    match cipher_choice:
        case "1":
            decrypt_affine()
        case "2":
            decrypt_caesar()
        case "3":
            decrypt_keyword()
        case "4":
            decrypt_polybius()
        case "5":
            decrypt_vigenere()
        case _:
            print("Invalid input. Exiting.")
            exit()


# Frequency analysis
def frequency_analysis():
    text = input("What text would you like to analyze?")
    analyze(text)
    pause = input("Press enter to continue.")


# Quick Modulo
def quick_modulo():
    # Prompt the user for input and convert the input to lowercase
    first = input("What is the first letter? ")
    first = first.lower()

    # Prompt the user for input and convert the input to lowercase
    second = input("What is the second letter? ")
    second = second.lower()

    # Call the "logic" function with the user input as arguments
    logic(first, second)
    pause = input("Press enter to continue.")


# begin encrypt functions


def encrypt_affine():
    plaintext = input("What is the text you would like to encrypt? ")
    a = int(input("Please input the first key. "))
    b = int(input("Please input the second key. "))
    affine_encrypt(plaintext, a, b)
    pause = input("Press enter to continue.")


def encrypt_caesar():
    plaintext = input("What is the plaintext you would like to encrypt? ")
    key = int(input("What is the key you would like to use? "))
    caeser_encrypt(plaintext, key)  # Call the encrypt function
    pause = input("Press enter to continue.")


def encrypt_keyword():
    plaintext = input("Enter the text you would like to encrypt: ")
    keyword = input("Enter the keyword you would like to use: ")
    keyword_encrypt(plaintext, keyword)
    pause = input("Press enter to continue.")


def encrypt_polybius():
    # Input plaintext to be encrypted
    plaintext = input("What is the plaintext? ")

    # Input the encryption keys (key2 and key1)
    # Note: The keys are input in this order due to a later code issue
    key2 = input("What is the first key? ")
    key1 = input("What is the second key? ")

    # Create the encryption square
    square = create_square()

    # Encrypt the plaintext
    ciphertext = polybius_encrypt(plaintext, square)

    # Apply the encryption keys to the ciphertext
    ciphertext = apply_key_enc(ciphertext, key1, key2)

    # Display the ciphertext
    print("The ciphertext is: " + ciphertext)
    pause = input("Press enter to continue.")


def encrypt_vigenere():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")
    viginere_encrypt(plaintext, key)  # Call the encrypt function
    pause = input("Press enter to continue.")


# begin decrypt functions
def decrypt_affine():
    ciphertext = input("What is the text you would like to decrypt? ")
    a = int(input("Please input the first key. "))
    b = int(input("Please input the second key. "))
    affine_decrypt(ciphertext, a, b)
    pause = input("Press enter to continue.")


def decrypt_caesar():
    key_or_crack = input(
        """Would you like to decrypt with a key or crack the cipher?
                     (1) Key
                     (2) Crack
                     """
    )
    match key_or_crack:
        case "1":
            ciphertext = input("What is the ciphertext you would like to decrypt? ")
            key = int(input("What is the key for the ciphertext? "))
            caesar_decrypt(ciphertext, key)  # Call the decrypt function
        case "2":
            ciphertext = input("What is the ciphertext you would like to crack? ")
            crack_caeser(ciphertext)  # Call the crack function
        case _:
            print("Invalid input. Exiting.")
            exit()
    pause = input("Press enter to continue.")


def decrypt_keyword():
    ciphertext = input("Enter the text you would like to decrypt: ")
    keyword = input("Enter the key you would like to use: ")
    keyword_decrypt(ciphertext, keyword)
    pause = input("Press enter to continue.")


def decrypt_polybius():
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
    plaintext = polybius_decrypt(ciphertext, square)

    print("The plaintext is: " + plaintext)
    pause = input("Press enter to continue.")


def decrypt_vigenere():
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key: ")
    viginere_decrypt(ciphertext, key)  # Call the decrypt function
    pause = input("Press enter to continue.")


main()

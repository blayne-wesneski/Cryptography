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

def main():
    function = input("""What would you like to do?
                     (1) Encrypt a message with a cipher?
                     (2) Decrypt a message with a cipher?
                     (3) Conduct a frequency analysis on a ciphertext?
                     """)
    match function:
        case "1":
            encrypt()
        case "2":
            decrypt()
        case "3":
            frequency_analysis()
        case _:
            print("Invalid input. Exiting.")
            exit()


def encrypt():
    cipher_choice = input("""What cipher would you like to encrypt with?
                     (1) Affine
                     (2) Caesar
                     (3) Keyword
                     (4) Polybius Square
                     (5) Vigenere
                     """)
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

def decrypt():
    cipher_choice = input("""What cipher would you like to decrypt with?
                     (1) Affine
                     (2) Caesar
                     (3) Keyword
                     (4) Polybius Square
                     (5) Vigenere
                     """)
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

def frequency_analysis():
    text = input("What text would you like to analyze?")


main()
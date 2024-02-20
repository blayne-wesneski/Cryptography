"""
Program Name: Ciphers
Author: Blayne Wesneski
Date: February 20th, 2024
Description: This program is a culmination of all the cipher programs I have written for my Cryptography class.
             It is made in order to cut down on the amount of Github Repos I have to manage.
             it allows the user to choose which cipher they would like to use and then encrypt or decrypt a message.
             It also contains the ability to conduct a frequency analysis on a given ciphertext.
"""

import sys

sys.path.insert(0, './Ciphers/Affine')
sys.path.insert(0, './Ciphers/Caeser')
sys.path.insert(0, './Ciphers/Keyword')
sys.path.insert(0, './Ciphers/Polybius Square')
sys.path.insert(0, './Ciphers/Viginere')
sys.path.insert(0, './Misc/Frequency Analysis')
sys.path.insert(0, './Misc/Quick Modulo')

from affine_driver import affine



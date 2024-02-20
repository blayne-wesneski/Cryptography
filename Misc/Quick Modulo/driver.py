"""
Program Name: Quick Modulo
Author: Blayne Wesneski
Date: November 15, 2023
Description: A very quick and dirty program written for my cryptography class that runs the equation P = (x - y) mod 26 given two letters.
"""

# Import the "logic" function from the "custom_logic" module
from custom_logic import logic

# Initialize an empty string for the letter
letter = ""

# Prompt the user for input and convert the input to lowercase
first = input("What is the first letter? ")
first = first.lower()

# Prompt the user for input and convert the input to lowercase
second = input("What is the second letter? ")
second = second.lower()

# Call the "logic" function with the user input as arguments
logic(first, second)

"""
Program Name: Frequency Analysis
Author: Blayne Wesneski
Date: September 20, 2023
Description: This program conducts a frequency analysis on a given text.
"""

# Prompt the user for input text
text = input("What text would you like to analyze? ")

# Clean the input text by removing non-alphabetic characters and converting to uppercase
text = ''.join(c for c in text if c.isalpha()).upper()

# Create an empty dictionary to store character frequencies
char_freq = {}

# Count the frequency of each character in the cleaned text
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Sort the character frequency dictionary by frequency in descending order
sorted_char_freq = dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True))

# Display the results
for char, frequency in sorted_char_freq.items():
    print(f"'{char}': {frequency}")
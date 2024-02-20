# Import the string module to get the lowercase alphabet
import string

# Initialize empty strings for the first and second input
first = ""
second = ""

# Initialize a variable to store the result of the logic
result = 0

# Create a dictionary to map each lowercase letter to its index in the alphabet
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index

# Create a reverse dictionary to map the index back to the corresponding letter
reverse_values = {index: letter for letter, index in values.items()}


# Define a function called "logic" that takes two letters as input
def logic(first, second):
    # Calculate the result using a formula based on the letter indices and modulo 26
    result = (values[first] - values[second]) % 26
    # Use the reverse dictionary to find the letter corresponding to the result
    letter = reverse_values[result]
    # Print the result
    print("The result is: " + letter)

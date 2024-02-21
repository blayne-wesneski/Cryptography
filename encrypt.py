# Affine Cipher encryption
def affine_encrypt(plaintext, a, b):
    encrypted_text = ""

    # Iterate through each character in the plaintext
    for char in plaintext:
        if char.isalpha():  # Check if the character is an alphabet character
            if char.islower():  # Check if the character is lowercase
                # Encrypt lowercase character and add it to the encrypted text
                encrypted_text += chr((a * (ord(char) - ord("a")) + b) % 26 + ord("a"))
            else:
                # Encrypt uppercase character and add it to the encrypted text
                encrypted_text += chr((a * (ord(char) - ord("A")) + b) % 26 + ord("A"))
        else:
            # Non-alphabet characters are added directly to the encrypted text
            encrypted_text += char

    # Print the encrypted text
    print(encrypted_text)


# Caesar Cipher encryption
def caeser_encrypt(plaintext, key):
    # Initialize the result variable to store the encrypted text
    result = ""

    # Loop through each character in the plaintext
    for i in range(len(plaintext)):
        char = plaintext[i]

        # Check for a space character
        if char == " ":
            result += " "  # Append space to the result

        # Encrypt uppercase characters
        elif char.isupper():
            result += chr(((ord(char)) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    # Print the encrypted message along with original plaintext and key
    print("The encrypted message is: " + result)
    print("The original plaintext is: " + plaintext)
    print("The key is: " + str(key))


# Keyword Cipher encryption


def keyword_encrypt(plaintext, keyword):
    # Remove duplicate characters from the keyword and convert to uppercase
    keyword = "".join(char for char in keyword.upper() if char != " ")
    keyword = "".join(dict.fromkeys(keyword.upper()))

    # Create a string of remaining letters (not in the keyword)
    remaining_letters = "".join(
        [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if char not in keyword]
    )

    # Create the key by combining the unique keyword characters and remaining letters
    key = keyword + remaining_letters

    # Convert the plaintext to uppercase for consistency
    plaintext = plaintext.upper()

    # Initialize an empty string to store the encrypted text
    ciphertext = ""

    # Iterate through each character in the plaintext
    for char in plaintext:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # If the character is a letter, find its position in the alphabet and
            # substitute it with the corresponding character from the key
            ciphertext += key[ord(char) - 65]
        else:
            # If the character is not a letter (e.g., space or punctuation), leave it unchanged
            ciphertext += char

    # Print the encrypted text
    print("The key is: " + key)
    print("The encrypted text is: " + ciphertext)


# Polybius Square encryption
def polybius_encrypt(plaintext, square):
    # Convert the plaintext to uppercase for case-insensitive matching
    plaintext = plaintext.upper()

    # Initialize an empty string for the ciphertext
    ciphertext = ""

    # Iterate through each character in the plaintext
    for char in plaintext:
        # Replace 'J' with 'I' (if encountered)
        if char == "J":
            char = "I"

        # Iterate through the rows and columns of the square to find the character's position
        for i in range(5):
            for j in range(5):
                # Check if the character in the square matches the current character in plaintext
                if square[i][j] == char:
                    # Append the row and column indices to the ciphertext
                    ciphertext += str(i) + str(j)

    # Return the resulting ciphertext
    return ciphertext


# Vigenere Cipher encryption
def viginere_encrypt(plaintext, key):
    # Initialize an empty string to store the ciphertext
    ciphertext = ""

    # Calculate the length of the key
    key_length = len(key)

    # Convert the key to uppercase for consistency
    key = key.upper()

    # Loop through each character in the plaintext
    for i, char in enumerate(plaintext):
        # Check if the character is an alphabetic character
        if char.isalpha():
            # Retrieve the corresponding character from the key based on the current position
            key_char = key[i % key_length]

            # Calculate the shift value by subtracting the ASCII values of key_char and 'A'
            shift = ord(key_char) - ord("A")

            # Check if the character is lowercase
            if char.islower():
                # Encrypt the lowercase character using the Caesar cipher formula
                encrypted_char = chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
            else:
                # Encrypt the uppercase character using the Caesar cipher formula
                encrypted_char = chr((ord(char) + shift - ord("A")) % 26 + ord("A"))

            # Add the encrypted character to the ciphertext
            ciphertext += encrypted_char

        else:
            # If the character is not alphabetic, keep it unchanged and add it to the ciphertext
            ciphertext += char

    # Print the ciphertext
    print("Ciphertext: " + ciphertext)

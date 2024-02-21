# Affine Cipher Decryption


# This function calculates the modular multiplicative inverse of 'a' modulo 'm'
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# This function decrypts the encrypted text using the provided keys 'a' and 'b'
def affine_decrypt(encrypted_text, a, b):
    decrypted_text = ""

    # Calculate the modular inverse of 'a' modulo 26
    a_inv = mod_inverse(a, 26)

    # Iterate through each character in the encrypted text
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is an alphabet character
            if char.islower():  # Check if the character is lowercase
                # Decrypt lowercase character and add it to the decrypted text
                decrypted_text += chr(
                    (a_inv * (ord(char) - ord("a") - b)) % 26 + ord("a")
                )
            else:
                # Decrypt uppercase character and add it to the decrypted text
                decrypted_text += chr(
                    (a_inv * (ord(char) - ord("A") - b)) % 26 + ord("A")
                )
        else:
            # Non-alphabet characters are added directly to the decrypted text
            decrypted_text += char

    # Print the decrypted text
    print(decrypted_text)


# Caeser Cipher Decryption
def caesar_decrypt(ciphertext, key):
    result = ""  # Initialize the variable to store the decrypted text

    # Loop through each character in the ciphertext
    for i in range(len(ciphertext)):
        char = ciphertext[i]

        # Check for a space character
        if char == " ":
            result += " "  # Append space to the result

        # Decrypt uppercase characters
        elif char.isupper():
            result += chr(((ord(char)) - key - 65) % 26 + 65)

        # Decrypt lowercase characters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)

    # Print the decrypted message
    print("The decrypted message is: " + result)
    print("The original ciphertext is: " + ciphertext)
    print("The key is: " + str(key))


# Keyword Cipher Decryption
def keyword_decrypt(ciphertext, keyword):
    # Remove duplicate characters and spaces from the keyword and convert it to uppercase
    keyword = "".join(char for char in keyword.upper() if char != " ")
    keyword = "".join(dict.fromkeys(keyword.upper()))

    # Create a string of remaining letters not in the keyword
    remaining_letters = "".join(
        [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if char not in keyword]
    )

    # Create the key by combining the unique keyword letters and remaining letters
    key = keyword + remaining_letters

    # Convert the ciphertext to uppercase
    ciphertext = ciphertext.upper()

    # Initialize an empty string for the decrypted plaintext
    plaintext = ""

    for char in ciphertext:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # Decrypt the character and append it to the plaintext
            plaintext += chr(key.index(char) + 65)
        else:
            # If the character is not an uppercase letter, append it as is
            plaintext += char

    # Print the decrypted plaintext
    print("The key is: " + key)
    print("The decrypted text is: " + plaintext)


# Polybius Square Decryption
def polybius_decrypt(ciphertext, square):
    # Initialize an empty string for the resulting plaintext
    plaintext = ""

    # Iterate through the ciphertext in pairs (two characters at a time)
    for i in range(0, len(ciphertext), 2):
        # Extract the row and column indices from the ciphertext and convert them to integers
        row = int(ciphertext[i])
        col = int(ciphertext[i + 1])

        # Retrieve the character from the square using the row and column indices
        plaintext += square[row][col]

    # return the resulting plaintext
    return plaintext


# Vigenere Cipher Decryption
def viginere_decrypt(ciphertext, key):
    # Initialize an empty string to store the plaintext
    plaintext = ""

    # Calculate the length of the key
    key_length = len(key)

    ciphertext = ciphertext.replace(" ", "")  # Remove spaces from the ciphertext

    # Loop through each character in the ciphertext
    for i, char in enumerate(ciphertext):
        # Check if the character is an alphabetic character
        if char.isalpha():
            # Retrieve the corresponding character from the key based on the current position
            key_char = key[i % key_length]

            # Calculate the shift value by subtracting the ASCII values of key_char and 'A'
            shift = ord(key_char) - ord("A")

            # Check if the character is lowercase
            if char.islower():
                # Decrypt the lowercase character using the reverse Caesar cipher formula
                decrypted_char = chr((ord(char) - shift - ord("a")) % 26 + ord("a"))
            else:
                # Decrypt the uppercase character using the reverse Caesar cipher formula
                decrypted_char = chr((ord(char) - shift - ord("A")) % 26 + ord("A"))

            # Add the decrypted character to the plaintext
            plaintext += decrypted_char
        else:
            # If the character is not alphabetic, keep it unchanged and add it to the plaintext
            plaintext += char

    # Print the plaintext
    print("Plaintext: " + plaintext)

def encrypt(plaintext, key):
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
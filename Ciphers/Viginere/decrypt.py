def decrypt(ciphertext, key):
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
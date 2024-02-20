def decrypt(ciphertext, square):
    # Initialize an empty string for the resulting plaintext
    plaintext = ""

    # Iterate through the ciphertext in pairs (two characters at a time)
    for i in range(0, len(ciphertext), 2):
        # Extract the row and column indices from the ciphertext and convert them to integers
        row = int(ciphertext[i])
        col = int(ciphertext[i+1])

        # Retrieve the character from the square using the row and column indices
        plaintext += square[row][col]

    #return the resulting plaintext
    return plaintext
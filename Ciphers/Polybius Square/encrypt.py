def encrypt(plaintext, square):
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
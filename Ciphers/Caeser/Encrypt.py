def encrypt(plaintext, key):
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
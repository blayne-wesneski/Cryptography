def decrypt(ciphertext, key):
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
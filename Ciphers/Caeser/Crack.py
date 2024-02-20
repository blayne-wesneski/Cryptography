def crack(ciphertext):
    # Ask for user confirmation before proceeding
    confirm = input(
        "This will list all possible shifts for you to choose the most likely candidate. Please enter [Y] to continue."
    )

    number = 0  # Initialize the count of decryption attempts
    result = ""  # Initialize the variable to store decrypted text

    # Loop through each possible shift value (1 to 26)
    for x in range(1, 27):
        # Iterate through each character in the ciphertext
        for i in range(len(ciphertext)):
            char = ciphertext[i]

            # Check for a space character
            if char == " ":
                result += " "  # Append space to the result

            # Decrypt uppercase characters
            elif char.isupper():
                result += chr(((ord(char)) - x - 65) % 26 + 65)

            # Decrypt lowercase characters
            else:
                result += chr((ord(char) - x - 97) % 26 + 97)

        number = number + 1  # Increment the decryption attempt count
        # Print the possible decryption along with its attempt number
        print("Possible decryption #" + str(number) + " is: " + result)
        result = ""  # Reset the result for the next attempt

def decrypt(ciphertext, keyword):
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

def encrypt(plaintext, keyword):
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

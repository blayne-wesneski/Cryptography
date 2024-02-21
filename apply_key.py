def apply_key_enc(ciphertext, key1, key2):
    # Convert the ciphertext string into a list of characters
    ciphertext_list = list(ciphertext)

    # Convert key1 and key2 to uppercase for case-insensitive matching
    key1 = key1.upper()
    key2 = key2.upper()

    # Convert key1 and key2 into lists of characters
    key1_list = list(key1)
    key2_list = list(key2)

    # Initialize an empty string for the modified ciphertext
    ciphertext = ""

    # Iterate through the characters in the ciphertext
    for i, char in enumerate(ciphertext_list):
        # Check if the character's position in the ciphertext is even (0, 2, 4, etc.)
        if i % 2 == 0:
            # If the character is a digit between 0 and 4, replace it with a character from key1
            if char in "01234":
                index = int(char)
                # Check if the index is within the bounds of key1_list
                if index < len(key1_list):
                    ciphertext += key1_list[index]
                else:
                    # If the index is out of bounds, keep the original character
                    ciphertext += char
            else:
                # If the character is not a digit between 0 and 4, keep it as is
                ciphertext += char
        else:
            # If the character's position in the ciphertext is odd (1, 3, 5, etc.), apply key2
            if char in "01234":
                index = int(char)
                # Check if the index is within the bounds of key2_list
                if index < len(key2_list):
                    ciphertext += key2_list[index]
                else:
                    # If the index is out of bounds, keep the original character
                    ciphertext += char
            else:
                # If the character is not a digit between 0 and 4, keep it as is
                ciphertext += char

    # Return the modified ciphertext
    return ciphertext


def apply_key_dec(ciphertext, key1, key2):
    
    # Convert the ciphertext string into a list of characters
    ciphertext_list = list(ciphertext)

    # Convert key1 and key2 to uppercase for case-insensitive matching
    key1 = key1.upper()
    key2 = key2.upper()

    # Convert key1 and key2 into lists of characters
    key1_list = list(key1)
    key2_list = list(key2)

    # Initialize an empty string for the resulting plaintext
    plaintext = ""

    # Iterate through the characters in the ciphertext
    for i, char in enumerate(ciphertext_list):
        # Check if the character's position in the ciphertext is even (0, 2, 4, etc.)
        if i % 2 == 0:
            # If the character is in key1_list, find its index in key1_list and append it to plaintext
            if char in key1_list:
                index = key1_list.index(char)
                plaintext += str(index)
            else:
                # If the character is not in key1_list, keep it as is
                plaintext += char
        else:
            # If the character's position in the ciphertext is odd (1, 3, 5, etc.), apply key2
            if char in key2_list:
                index = key2_list.index(char)
                plaintext += str(index)
            else:
                # If the character is not in key2_list, keep it as is
                plaintext += char

    # Return the resulting plaintext
    return plaintext

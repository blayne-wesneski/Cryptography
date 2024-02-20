# This function encrypts the provided plaintext using the provided keys 'a' and 'b'
def encrypt(plaintext, a, b):
    encrypted_text = ""
    
    # Iterate through each character in the plaintext
    for char in plaintext:
        if char.isalpha():  # Check if the character is an alphabet character
            if char.islower():  # Check if the character is lowercase
                # Encrypt lowercase character and add it to the encrypted text
                encrypted_text += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            else:
                # Encrypt uppercase character and add it to the encrypted text
                encrypted_text += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
        else:
            # Non-alphabet characters are added directly to the encrypted text
            encrypted_text += char
    
    # Print the encrypted text
    print(encrypted_text)
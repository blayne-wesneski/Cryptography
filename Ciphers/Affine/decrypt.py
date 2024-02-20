# This function calculates the modular multiplicative inverse of 'a' modulo 'm'
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# This function decrypts the encrypted text using the provided keys 'a' and 'b'
def decrypt(encrypted_text, a, b):
    decrypted_text = ""
    
    # Calculate the modular inverse of 'a' modulo 26
    a_inv = mod_inverse(a, 26)
    
    # Iterate through each character in the encrypted text
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is an alphabet character
            if char.islower():  # Check if the character is lowercase
                # Decrypt lowercase character and add it to the decrypted text
                decrypted_text += chr((a_inv * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            else:
                # Decrypt uppercase character and add it to the decrypted text
                decrypted_text += chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A'))
        else:
            # Non-alphabet characters are added directly to the decrypted text
            decrypted_text += char
    
    # Print the decrypted text
    print(decrypted_text)
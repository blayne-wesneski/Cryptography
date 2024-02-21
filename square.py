def create_square():
    # Define the alphabet without the letter 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Create a 5x5 square filled with spaces
    square = [[' ' for i in range(5)] for j in range(5)]
    
    # Initialize an index to track the position in the alphabet
    index = 1
    
    # Fill the square with characters from the alphabet
    for i in range(5):
        for j in range(5):
            # Assign the current character from the alphabet to the square
            square[i][j] = alphabet[index-1]
            
            # Increment the index to move to the next character in the alphabet
            index += 1
    
    # Return the completed square
    return square
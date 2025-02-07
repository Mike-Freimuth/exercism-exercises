def rows(letter):
    
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    letter_index = letters.index(letter)
    outside_space = letter_index
    inside_space = 1
    letter = 0
    diamond = [' ' * outside_space + letters[letter] + ' ' * outside_space]
    
    while outside_space > 0:
        
        letter += 1
        outside_space -= 1
        diamond.append(' ' * outside_space + letters[letter] + ' ' * inside_space + letters[letter] + ' ' * outside_space)
        inside_space += 2
        
    inside_space -= 4
    
    while outside_space < letter_index - 1:
        
        letter -= 1
        outside_space += 1
        diamond.append(' ' * outside_space + letters[letter] + ' ' * inside_space + letters[letter] + ' ' * outside_space)
        inside_space -= 2
    
    if letter_index > 0:
            
        diamond.append(' ' * letter_index + letters[0] + ' ' * letter_index)
    
    return diamond
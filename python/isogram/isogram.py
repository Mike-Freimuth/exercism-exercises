def is_isogram(string):
    
    letters = set()
    exceptions = {' ', '-'}
    
    for letter in string.lower():
        
        if letter not in(exceptions):
        
            if letter in letters:
                return False
            
            letters.add(letter)
        
    return True
        

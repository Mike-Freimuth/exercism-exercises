def is_valid(isbn):
    
    if len(isbn) < 10:
        return False
    
    digits = []
    
    for character in isbn[:-1]:
        
        if character not in {'0','1','2','3','4','5','6','7','8','9','10','-'}:
            return False
        
        if character != '-':
            digits.append(int(character))
            
    if isbn[-1] == 'X':
        digits.append(10)
        
    elif isbn[-1] not in {'0','1','2','3','4','5','6','7','8','9','10'}:
        return False
        
    else: 
        digits.append(int(isbn[-1]))
        
    if len(digits) != 10:
        return False
        
    checksum = 0
    multiplier = 10
    
    for digit in digits:
        checksum += digit * multiplier
        multiplier -= 1
        
    return checksum % 11 == 0

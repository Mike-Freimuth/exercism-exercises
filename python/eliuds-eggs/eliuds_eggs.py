import math

def egg_count(display_value):
    
    if display_value < 2:
        return display_value
    
    number = display_value
    binary = ''
    
    for i in range(int(math.log2(display_value)), -1, -1):
        
        if number >= 2**i:
            binary += '1'
            number -= 2**i
            
        else:
            binary += '0'
            
    count = 0
            
    for digit in binary:
        
        if digit == '1':
            count += 1
            
    return count

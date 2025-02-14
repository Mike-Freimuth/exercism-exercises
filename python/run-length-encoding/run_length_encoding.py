def decode(string):
    
    number = ''
    decoded = ''
    
    for character in string:
        
        if character.isnumeric():
            number += character
            
        else:
            
            if number == '':
                decoded += character
            
            else:    
                decoded += character * int(number)
                number = ''
                
    return decoded
            
            

def encode(string):
    
    counter = 1
    encoded = ''
    
    if len(string) == 0:
        return encoded
    
    for i in range (1, len(string)):
        
        if string[i] == string[i-1]:
            counter += 1
            
        else:
            
            if counter > 1:
                encoded += str(counter)
                counter = 1
            
            encoded += string[i-1]
            
    if counter > 1:
                encoded += str(counter)
                counter = 1
            
    encoded += string[-1]
    
    return encoded
def rotate(text, key):
    
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    message = ''
    
    for character in text:
        
        if character.isalpha():
            
            if character.islower():
                message += letters[(letters.index(character) + key) % 26]
                
            else:
                message += letters[(letters.index(character.lower()) + key) % 26].upper()
                
        else:
            message += character

    return message
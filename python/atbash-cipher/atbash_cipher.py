letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher = {}

for index in range(26):
    cipher[letters[index]] = letters[-(index+1)]
    
decoder = {}

for item in cipher.items():
    decoder[item[1]] = item[0]
    

def encode(plain_text):
    
    encoded = ''
    counter = 0
    
    for character in plain_text.lower():
        
        if counter == 5:
            encoded += ' '
            counter = 0
        
        if character in letters:
            encoded += cipher[character]
            counter += 1
            
        if character.isnumeric():
            encoded += character
            counter += 1
            
    while encoded[-1] == ' ':
        encoded = encoded[:-1]
            
    return encoded


def decode(ciphered_text):
    
    decoded = ''
    
    for character in ciphered_text:
        
        if character != ' ':
            
            if character.isnumeric():
                decoded += character
                
            else:
                decoded += decoder[character]
            
    return decoded

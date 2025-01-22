def commands(binary_str):

    things = ['jump', 'close your eyes', 'double blink', 'wink']
    place = 0
    handshake = []

    for i in binary_str[-4:]:
        
        if i == '1':
            handshake.append(things[place])
            
        place += 1    

    if binary_str[-5] == '0':
        handshake.reverse()
    
    return handshake
def is_paired(input_string):
    
    types = {
        '[' : ']', 
        '(' : ')', 
        '{' : '}'
        }
    
    closed = True
    open = []

    for character in input_string:
        
        if character in ['[', ']', '(', ')', '{', '}']:
            
            if closed == True:
                
                if character in [']', ')', '}']:
                    return False
                
                closed = False
                open.append(character)
                
            else:
                
                if character in [']', ')', '}']:
                    
                    if character == types[open[-1]]:
                        
                        open.pop()
                        
                        if len(open) == 0:
                            closed = True
                            
                    else:
                        return False
                    
                else:
                    
                    closed = False
                    open.append(character)
    
    if closed == False:
        return False
    
    return True
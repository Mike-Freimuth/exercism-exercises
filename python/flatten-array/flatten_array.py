def flatten(iterable):
    
    flat = []
    
    for item in iterable:
        
        if item == None:
            continue
        
        elif type(item) == int:
            flat += [item]

        else:
            flat += flatten(item)
            
    return flat
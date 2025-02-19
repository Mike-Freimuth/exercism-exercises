def proverb(*args, qualifier=None):
    
    things = [arg for arg in args]
    output = []
    
    if len(things) == 0:
        return output
    
    for i in range(len(things) - 1):
        
        output.append(f'For want of a {things[i]} the {things[i+1]} was lost.')
        
    if qualifier == None:
        qualifier = ''
        
    else:
        qualifier += ' '
        
    output.append(f'And all for the want of a {qualifier}{things[0]}.')

    return output
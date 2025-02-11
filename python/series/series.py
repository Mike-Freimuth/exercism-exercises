def slices(series, length):
    
    if length == 0:
        raise ValueError("slice length cannot be zero")
    
    if length < 0:
        raise ValueError("slice length cannot be negative")
    
    if series == None or series == '':
        raise ValueError("series cannot be empty")
    
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    output = []
    
    for i in range(len(series) - length + 1):
        output.append(series[i:i+length])
        
    return output
        

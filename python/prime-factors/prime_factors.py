def factors(value):
    
    factors = []
    candidate = 2
    
    while value > 1:
        
        if value % candidate == 0:
            factors.append(candidate)
            value = value / candidate
            
        else:
            candidate += 1

    return factors
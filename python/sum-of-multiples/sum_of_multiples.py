def sum_of_multiples(limit, multiples):
    
    set_of_multiples = set()
    
    for factor in multiples:
        
        if factor == 0:
            continue
        
        multiple = factor
        
        while multiple < limit:
            set_of_multiples.add(multiple)
            multiple += factor
            
    return sum(set_of_multiples)

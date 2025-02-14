def prime(number):
    
    if number < 1:
        raise ValueError('there is no zeroth prime')
    
    primes = []
    candidate = 2
    
    while len(primes) < number:
        
        prime = True
        
        for x in primes:
            
            if candidate % x == 0:
                prime = False
                break

        if prime:
            primes.append(candidate)
            
        candidate += 1
        
    return primes[-1]
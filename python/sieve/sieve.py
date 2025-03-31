def primes(limit):
    
    numbers = {}
    
    for number in range(2, limit + 1):
        numbers[number] = 'prime'
        
    for i in range(2, limit +1):
        
        if numbers[i] == 'prime':
            
            multiple = 2 * i
            while multiple <= limit:
                
                numbers[multiple] = 'not prime'
                multiple += i
                
    primes = []       
    
    for number in numbers.keys():
        if numbers[number] == 'prime':
            primes.append(number)
            
    return primes
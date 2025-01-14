def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number % 1 != 0 or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    if number == 1:
        return 'deficient'
    
    factors = [1]
    
    for i in range(2, int(number**0.5) + 1):
        
        if number % i == 0:
            factors.append(i)
            
            if number / i != i:
                factors.append(number / i)
            
    sum_of_factors = sum(factors)
    
    if sum_of_factors == number:
        return 'perfect'
    
    if sum_of_factors > number:
        return 'abundant'
    
    return 'deficient'

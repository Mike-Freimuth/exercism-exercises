def is_armstrong_number(number):
    
    digits = len(str(number))
    
    compare = 0
    for digit in str(number):
        compare += int(digit) ** digits
        
    return number == compare

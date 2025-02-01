def square_root(number):
    
    x = number 
    
    while True:
        
        if x*x == number:
            return x
        
        x = (x + (number/x)) // 2

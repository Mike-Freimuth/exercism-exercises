def leap_year(year):
    
    if year % 4 != 0:
        return False
    
    if year % 100 == 0:
        
        if year % 400 != 0:
            return False
        
    return True

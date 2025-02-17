def roman(number):
    
    if number >= 1000:
        return 'M' + roman(number - 1000)
    
    if number >= 900:
        return 'CM' + roman(number - 900)
    
    if number >= 500:
        return 'D' + roman(number - 500)
    
    if number >= 400:
        return 'CD' + roman(number - 400)
    
    if number >= 100:
        return 'C' + roman(number -100)
    
    if number >= 90:
        return 'XC' + roman(number - 90)
    
    if number >= 50:
        return 'L' + roman(number - 50)
    
    if number >= 40:
        return 'XL' + roman(number - 40)
    
    if number >= 10:
        return 'X' + roman(number - 10)
    
    if number == 9:
        return 'IX'
    
    if number >= 5:
        return 'V' + roman(number - 5)
    
    if number == 4:
        return 'IV'
    
    if number >= 1:
        return 'I' + roman(number -1)
    
    if number == 0:
        return ''


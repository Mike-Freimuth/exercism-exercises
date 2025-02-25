class PhoneNumber:
    def __init__(self, number):
        
        remove = ['+', '-', '(', ')', '.', ' ']
        
        for character in remove:
            number = number.replace(character, '')
            
        for character in number:
            
            if character.isalpha():
                raise ValueError("letters not permitted")
            
        if number.isnumeric() == False:
            raise ValueError("punctuations not permitted")
        
        length = len(number)
        
        if length < 10:
            raise ValueError("must not be fewer than 10 digits")
        
        if length > 11:
            raise ValueError("must not be greater than 11 digits")
        
        if length == 11:
            
            if number[0] != '1':
                raise ValueError("11 digits must start with 1")
        
            number = number[1:]
            
        if number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        
        if number[3] == '1':
            raise ValueError("exchange code cannot start with one")
        
        if number[0] == '0':
            raise ValueError("area code cannot start with zero")
        
        if number[0] == '1':
            raise ValueError("area code cannot start with one")
            
        self.number = number
        
        self.area_code = number[0:3]
        
    def pretty(self):
        return '(' + self.number[0:3] + ')' + '-' + self.number[3:6] + '-' + self.number[6:]
    
    
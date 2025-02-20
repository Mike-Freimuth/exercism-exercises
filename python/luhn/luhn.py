class Luhn:
    def __init__(self, card_num):
        
        self.card_num = card_num

    def valid(self):
        
        number = self.card_num.replace(' ', '')
        n = len(number)
        if n < 2:
            return False
        
        if number.isdigit() == False:
            return False
        
        def replace(number):
            
            if 2*number > 9:
                return 2*number - 9
            
            else:
                return 2*number
            
        validation_number = ''
        
        for i in range(n):
            
            if i % 2 == 0:
                validation_number = number[n-1-i] + validation_number
                
            else:
                validation_number = str(replace(int(number[n-1-i]))) + validation_number
                
        sum = 0
        
        for character in validation_number:
            sum += int(character)
        
        if sum % 10 == 0:
            return True
        
        return False
            

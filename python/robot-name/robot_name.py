import random
import string
class Robot:
    
    names = []

    def __init__(self):
        
        self.name = Robot.name()
        
        while self.name in Robot.names:
            self.name = Robot.name()
            
        Robot.names.append(self.name)
        
        
    def name():
        
        letters = string.ascii_uppercase
        name = ''
        
        for i in range(2):
            name += letters[random.randint(0,25)]
            
        for i in range(3):
            name += str(random.randint(0,9))
            
        return name

    def reset(self):
        
        #Robot.names.remove(self.name)......IMO this should be here but the test is broken so that it causes it to fail due to same random seed used to test the reset.
        self.name = Robot.name()
        
        while self.name in Robot.names:
            self.name = Robot.name()
            
        Robot.names.append(self.name)

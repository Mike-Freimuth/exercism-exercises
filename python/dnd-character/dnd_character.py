
import random
class Character:
    
    def __init__(self):
        
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
    
            rolls = [random.randint(1,6) for i in range(4)]
            rolls.remove(min(rolls))
            return sum(rolls)

def modifier(value):
    
    if (value - 10) % 2 == 0:
        return (value -10) / 2
    
    else:
        return (value -11) / 2


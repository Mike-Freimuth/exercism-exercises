# Globals for the directions
# Change the values as you see fit

NORTH = 0
SOUTH = 2
EAST = 1
WEST = 3

directions = [NORTH, EAST, SOUTH, WEST,]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        
        self.direction_index = directions.index(direction)
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos, y_pos)
        
    def move(self, instructions):
        
        for instruction in instructions:
            
            if instruction == 'R':
                
                self.direction_index = (self.direction_index + 1) % 4
                self.direction = directions[self.direction_index]
                
            if instruction == 'L':
                
                self.direction_index = (self.direction_index - 1) % 4
                self.direction = directions[self.direction_index]
        
            if instruction == 'A':
                
                if self.direction == NORTH:
                    self.y_pos += 1
                    
                if self.direction == SOUTH:
                    self.y_pos -= 1
                    
                if self.direction == EAST:
                    self.x_pos += 1
                    
                if self.direction == WEST:
                    self.x_pos -= 1
                    
        self.coordinates = (self.x_pos, self.y_pos)
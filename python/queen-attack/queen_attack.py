class Queen:
    def __init__(self, row, column):
                
        if row < 0:
            raise ValueError("row not positive")
        
        if row > 7:
            raise ValueError("row not on board")
        
        if column < 0:
            raise ValueError("column not positive")
        
        if column > 7:
            raise ValueError("column not on board")
        
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        
        if self.row < 0 or another_queen.row < 0:
            raise ValueError("row not positive")
        
        if self.row > 8 or another_queen.row > 8:
            raise ValueError("row not on board")
        
        if self.column < 0 or another_queen.column < 0:
            raise ValueError("column not positive")
        
        if self.column > 8 or another_queen.column > 8:
            raise ValueError("column not on board")
        
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        
        if self.row - another_queen.row == self.column - another_queen.column:
            return True
        
        if self.row - another_queen.row == another_queen.column - self.column:
            return True
        
        return False

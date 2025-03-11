def saddle_points(matrix):
    
    if len(matrix) == 0:
        return []
    
    columns = len(matrix[0])
    
    for row in matrix:
        if len(row) != columns:
            raise ValueError("irregular matrix")
        
    row_max = []
    
    for row in matrix:
        
        max = 0
        max_index = []
        
        for i in range(columns):
            
            if row[i] > max:
                max = row[i]
                max_index = [i]
                
            elif row[i] == max:
                max_index.append(i)
                
        row_max.append(max_index)
            
    potential_houses = []
    
    for i in range(len(row_max)):
        
        if len(row_max[i]) > 0:
            
            for j in row_max[i]:
            
                candidate_height = matrix[i][j]
                column_min = True
                for row in matrix:
                    
                    if row != matrix[i] and row[j] < candidate_height:
                        column_min = False
                        break
                    
                if column_min == True:
                    potential_houses.append({'row' : i + 1, 'column' : j + 1})
        
    return potential_houses

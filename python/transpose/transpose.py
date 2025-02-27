def transpose(text):
    
    rows = text.split('\n')
    max_length = max([len(row) for row in rows])

    for i in range(len(rows)):
        
        rows[i] = rows[i] + '@'*(max_length - len(rows[i]))
        
    transpose = [character for character in rows[0]]
    
    for i in range(1,len(rows)):
        for j in range(max_length):
            
            transpose[j] += rows[i][j]
            
    for i in range(len(transpose)):
        transpose[i] = transpose[i].rstrip('@').replace('@',' ')
            
    return '\n'.join(transpose)
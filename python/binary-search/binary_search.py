def find(search_list, value):
    
    if len(search_list) == 0 or search_list[-1] < value or search_list[0] > value:
        raise ValueError("value not in array")
    
    lower = 0
    upper = len(search_list) - 1
    
    while upper - lower > 1:
        
        middle = (upper + lower) // 2
        
        if search_list[middle] == value:
            return middle
        
        if search_list[middle] < value:
            lower = middle
            
        else:
            upper = middle

    if search_list[upper] == value:
        return upper
    
    if search_list[lower] == value:
        return lower
    
    raise ValueError("value not in array")
def append(list1, list2):
    
    return list1 + list2


def concat(lists):
    
    flat = []
    
    for item in lists:
        
        for i in item:
            flat.append(i)
            
    return flat


def filter(function, list):
    
    filtered = []
    
    for item in list:
        
        if function(item) == True:
            filtered.append(item)
            
    return filtered


def length(list):
    
    counter = 0
    
    for item in list:
        counter += 1
        
    return counter

def map(function, list):
    
    new_list = []
    
    for i in range(len(list)):
        new_list.append(function(list[i]))

    return new_list

def foldl(function, list, initial):
    
    accumulator = initial
    
    for item in list:
        accumulator = function(accumulator, item)
        
    return accumulator


def foldr(function, list, initial):
    
    accumulator = initial
    
    for index in range(len(list) - 1, -1, -1):
        accumulator = function(accumulator, list[index])
        
    return accumulator


def reverse(list):
    
    reversed_list = []
    
    for item in list:
        reversed_list.insert(0,item)
        
    return reversed_list

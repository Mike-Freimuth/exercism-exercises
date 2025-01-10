def equilateral(sides):
    
    return sides[0] > 0 and sides[1] == sides[0] and sides[2] == sides[0]


def isosceles(sides):
    
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    side_comparisons = [sides[0] + sides[1] <= sides[2], sides[0] + sides[2] <= sides[1], sides[1] + sides[2] <= sides[0]]
    
    for x in side_comparisons:
        if x:  return False
        
    
    if len(set(x for x in sides)) == 3:
        return False
    
    return True


def scalene(sides):
        
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    
    side_comparisons = [sides[0] + sides[1] <= sides[2], sides[0] + sides[2] <= sides[1], sides[1] + sides[2] <= sides[0]]
    
    for x in side_comparisons:
        if x:  return False
    
    if len(set(x for x in sides)) < 3:
        return False
    
    return True

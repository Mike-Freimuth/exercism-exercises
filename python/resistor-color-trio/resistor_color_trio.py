def label(colors):
    
    resistor_values = {
        'black' : 0,
        'brown' : 1,
        'red' : 2,
        'orange' : 3,
        'yellow' : 4,
        'green' : 5,
        'blue' : 6,
        'violet' : 7,
        'grey' : 8,
        'white' : 9,
    }
    
    output = str(resistor_values[colors[0]]) + str(resistor_values[colors[1]])
    
    for x in range(resistor_values[colors[2]]):
        output += '0'
        
    output = str(int(output))
    
    trailing_zeros = resistor_values[colors[2]]
    if colors[1] == 'black':
        trailing_zeros += 1
    
    if trailing_zeros >= 9:
        return output[:-9] + ' gigaohms'
    
    if trailing_zeros >= 6:
        return output[:-6] + ' megaohms'
    
    if trailing_zeros >= 3:
        return output[:-3] + ' kiloohms'
    
    return output + ' ohms'

def value(colors):
    
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
    
    return int(output)
    
    

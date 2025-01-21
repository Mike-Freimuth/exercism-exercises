def resistor_label(colors):
    
    if len(colors) == 1:
        return '0 ohms'
    
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
    
    tolerance ={
        'silver': 10,
        'gold' : 5,
        'red' : 2,        
        'brown' : 1,
        'green' : .5,
        'blue' : .25,
        'violet' : .1,
        'grey' : .05,
    }
    
    output = str(resistor_values[colors[0]]) + str(resistor_values[colors[1]])
    
    if len(colors) == 4:
    
        for x in range(resistor_values[colors[2]]):
            output += '0'
            
    if len(colors) == 5:
        
        output += str(resistor_values[colors[2]])
        
        for x in range(resistor_values[colors[3]]):
            output += '0'
            
    output = int(output)
    
    if output >= 1000000000:
        
        if output/1000000000 % 1 == 0:
            output = str(int(output/1000000000)) + ' gigaohms'
            
        else:
            output = str(output/1000000000) + ' gigaohms'

    elif output >= 1000000:
        
        if output/1000000 % 1 == 0:
            output = str(int(output/1000000)) + ' megaohms'
            
        else:
            output = str(output/1000000) + ' megaohms'
        
    elif output >= 1000:
        
        if output/1000 % 1 == 0:
            output = str(int(output/1000)) + ' kiloohms'
            
        else:
            output = str(output/1000) + ' kiloohms'
        
    else:
        output = str(output) + ' ohms'

        
    return output + ' \xB1{}%'.format(tolerance[colors[-1]])

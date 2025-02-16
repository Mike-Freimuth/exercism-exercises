def recite(start_verse, end_verse):
    
    gifts = [
        ['first', 'a Partridge in a Pear Tree.'],
        ['second', 'two Turtle Doves, '],
        ['third', 'three French Hens, '],
        ['fourth', 'four Calling Birds, '],
        ['fifth', 'five Gold Rings, '],
        ['sixth', 'six Geese-a-Laying, '],
        ['seventh', 'seven Swans-a-Swimming, '],
        ['eighth', 'eight Maids-a-Milking, '],
        ['ninth', 'nine Ladies Dancing, '],
        ['tenth', 'ten Lords-a-Leaping, '],
        ['eleventh', 'eleven Pipers Piping, '],
        ['twelfth', 'twelve Drummers Drumming, '],
    ]

    def verse(day):
        
        verse = f'On the {gifts[day-1][0]} day of Christmas my true love gave to me: '
        
        for i in range(day-1, 0, -1):
            verse += gifts[i][1]
            
        if day > 1:
            verse += 'and ' + gifts[0][1]
        
        else:    
            verse += gifts[0][1]
            
        return verse
        
    verses = [verse(start_verse)]
    
    for j in range(start_verse + 1, end_verse + 1):
        verses.append(verse(j))
        
    return verses
    
    
        
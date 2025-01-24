def recite(start_verse, end_verse):
    things = [
        ['horse and the hound and the horn'],
        ['farmer sowing his corn', 'belonged to'],
        ['rooster that crowed in the morn', 'kept'],
        ['priest all shaven and shorn', 'woke'],
        ['man all tattered and torn', 'married'],
        ['maiden all forlorn', 'kissed'],
        ['cow with the crumpled horn', 'milked'],
        ['dog', 'tossed'],
        ['cat', 'worried'],
        ['rat', 'killed'],
        ['malt', 'ate'],
        ['house that Jack built.', 'lay in']
            ]

    def verse(number):
        
        if number == 1:
            return "This is the house that Jack built."
        
        first_line = 'This is the {}'
        other_line = ' that {} the {}'
        
        lines = first_line.format(things[-number][0])
        
        for i in range(number-1, 0, -1):
            
            lines += other_line.format(things[-i][1], things[-i][0])
            
        return lines
    
    verses = []

    for j in range(start_verse, end_verse+1):
        
        verses.append(verse(j))
        
    return verses
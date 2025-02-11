def abbreviate(words):
    
    acronym = []
    
    for word in words.split():
        
        index = 0
        length_of_word = len(word)
        not_a_word = False
        
        while word[index].isalpha() == False:
            index+=1
            if index > length_of_word - 1:
                not_a_word = True
                break
            
        if not_a_word:
            continue
        
        acronym.append(word[index].upper())
        
        if '-' in word:
            
            more_words = word.split('-')[1:]
            
            for word in more_words:
                acronym.append(word[0].upper())

    return ''.join(acronym)
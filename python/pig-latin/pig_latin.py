def translate(text):
    
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    pl_text = []
    
    for word in text.split():

        if word[0] in vowels or word[:2].lower() in ['xr', 'yt']:
            pl_text.append(word + 'ay')
        
        else:
            beginning = word[0]
            character = 1
            while word[character] not in vowels + ['y','Y']:
                beginning += word[character]
                character += 1
                
            if word[character] == 'u' and beginning[-1] in ['q','Q']:
                beginning += 'u'
                character += 1
                
            pl_text.append(word[character:] + beginning + 'ay')
        
    return ' '.join(pl_text)
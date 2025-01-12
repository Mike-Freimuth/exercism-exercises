def response(hey_bob):
    
    characters = set(hey_bob)
    
    if len(hey_bob) == 0 or hey_bob.isspace():
        return 'Fine. Be that way!'
    
    question = hey_bob.strip()[-1] == '?'
        
    yelling = any(c.isalpha() for c in hey_bob) and hey_bob.upper() == hey_bob
    '''
    characters.isdisjoint({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
    '''
    
    if question and yelling:
        return "Calm down, I know what I'm doing!"
    
    if question:
        return 'Sure.'
    
    if yelling:
        return 'Whoa, chill out!'
    
    return 'Whatever.'
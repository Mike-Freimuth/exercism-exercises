def is_pangram(sentence):
    
    letters = set('abcdefghijklmnopqrstuvwxyz')
    
    return letters.issubset(set(sentence.lower()))

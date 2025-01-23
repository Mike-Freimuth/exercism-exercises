def find_anagrams(word, candidates):
    
    def make_dictionary(word):
        
        letters = {}
    
        for letter in word.lower():
            
            if letter in letters.keys():
                letters[letter] += 1
                
            else:
                letters[letter] = 1
                
        return letters
    
    letters = make_dictionary(word)
    anagrams = []
    
    for candidate in candidates:
        
        if candidate.lower() == word.lower():
            continue
        
        if make_dictionary(candidate) == letters:
            anagrams.append(candidate)
            
    return anagrams

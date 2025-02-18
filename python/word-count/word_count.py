import string

def count_words(sentence):
    
    punctuation = string.punctuation.replace("'", "")
    map = str.maketrans(punctuation, ' ' * len(punctuation))
    words = sentence.translate(map).lower().split()
    word_count = {}
    
    for word in words:
        
        word = word.strip("'")
        if len(word) == 0:
            continue
        
        if word in word_count.keys():
            word_count[word] += 1
            
        else:
            word_count[word] = 1
            
    return word_count
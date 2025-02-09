def proteins(strand):
    
    encoding = {
        'AUG' : 'Methionine',
        'UUU' : 'Phenylalanine',
        'UUC' : 'Phenylalanine',
        'UUA' : 'Leucine',
        'UUG' : 'Leucine',
        'UCU' : 'Serine',
        'UCC' : 'Serine',
        'UCA' : 'Serine',
        'UCG' : 'Serine',
        'UAU' : 'Tyrosine',
        'UAC' : 'Tyrosine',
        'UGU' : 'Cysteine',
        'UGC' : 'Cysteine',
        'UGG' : 'Tryptophan',
        'UAA' : 'STOP',
        'UAG' : 'STOP',
        'UGA' : 'STOP'
    }

    proteins = []
    
    while len(strand) > 2:
        
        if encoding[strand[:3]] == 'STOP':
            break
        
        proteins.append(encoding[strand[:3]])
        strand = strand[3:]
        
    return proteins
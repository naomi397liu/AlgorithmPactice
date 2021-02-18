def unscramble(wordlist, keypads):
    ''' takes in a list of words as strings and takes in
    keypads that are lists of 7 scrambled letters, return a list of integers that tell you
    how many words from the wordlist you can make out of the letters in that keypad '''

    words = []
    word_count = [0]

    for word in wordlist:
        words.append(set(word))
        
    for i, keypad in enumerate(keypads): #'PBNEDAL'
        word_count.append(0) #[0]
        for word in words: #'PLEA'
            num_letters = 0 
            for j in range(0, len(keypad)):#0-7, 0, 1, 2, 3, 4, 5, 6
                if keypad[j] in word: #P, B-NO, N-NO, E, D-NO, A, L
                    num_letters += 1 #1, 2, 3, 4
            if num_letters == len(word):
                word_count[i] += 1
    return word_count

wordlist = ['PLEA', 'PLEASE', 'APPLE', 'DOG']
keypads = ['PBNEDAL', 'OESADLP', 'MOTLAJF', 'GBLKORD'] #[2,3,0,1]

# print(unscramble(wordlist, keypads))



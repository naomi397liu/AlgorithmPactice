def fun(wordlist, keypads):
    ''' takes in a list of words as strings that are 5 letters long or more and takes in
    keypads that are lists of 7 scrambled letters, return a list of integers that tell you
    how many words from the wordlist you can make out of the letters in that keypad '''
wordlist = ['PLEA', 'PLEASE', 'APPLE', 'DOG']
keypads = ['PBNEDAL', 'OESADLP', 'MOTLAJF', 'GBLKORD'] #[2,3,0,1]
words = []

word_count = [0]

for word in wordlist:
    words.append(set(word))
    
for i, keypad in enumerate(keypads):
    word_count.append(0)
    for word in words:
        num_letters = 0
        for j in range(len(keypad)):
            if keypad[j] in word:
                num_letters += 1
        if num_letters > 4:
            word_count[i] += 1
print(word_count)

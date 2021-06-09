class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        '''
        transform each word into its morse code version 
        put the words in a set and return the length of the set
        
        
        '''
        dictionary ={}
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = string. ascii_lowercase
        for i, m in enumerate(morse):
            dictionary[alphabet[i]] = m
        translated = set()
        for word in words:
            new_word = []
            for letter in word:
                new_word.append(dictionary[letter])
            translated.add("".join(new_word))
        return len(translated)
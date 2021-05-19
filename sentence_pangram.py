class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        given a string, return true if every letter of the alphbet shows up once
        put all the letters in a set
        see if the length of the set is 26, if so return true.
        
        '''
        letters = set(sentence)
        return len(letters) == 26
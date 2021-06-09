class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        '''
        split the strings with slicing
        create a list of vowels
        iterate thru both lists and compare the sum of vowels
        
        
        '''
        
        a = s[:int(len(s)/2)]
        b = s[int(len(s)/2):]
        vowels = set('aeiouAEIOU')
        a_count = 0
        b_count = 0
        for letter in a:
            if letter in vowels:
                a_count+=1
        for letter in b:
            if letter in vowels:
                b_count+=1
    
        return b_count == a_count
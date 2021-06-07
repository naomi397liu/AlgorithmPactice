import string
string.ascii_lowercase
class Solution:
    def replaceDigits(self, s: str) -> str:
        '''
        what's 0-indexed?
        is 0 even or odd?  - even?
        even indicies -lower
        odd indicies - digits 
        
        goal:
        replace each odd index with shift(s[i-1],s[i])
        return s
        
        plan of action:
        iterate thru odds in s
        and replace with shift(s[i-1],s[i])
        
        edge case:
        what happens if it exceeds z? it is guarenteed to not -> fuction takes care of it
        
        '''
        letters = {}
        for i, letter in enumerate(list(string.ascii_lowercase)):
            letters[letter] = int(i)
            
        def shift(start, distance):
            index = int(letters[start]) + int(distance)
            if index > 26:
                index = index%26
            for letter in letters.keys():
                if letters[letter] == index:
                    new_letter = letter
            return str(new_letter)
        
        s = list(s)
    
        for i in range(1, len(s), 2):
            s[i] = shift(s[i-1],s[i])
        return "".join(s)
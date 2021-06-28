class Solution:
    def sortString(self, s: str) -> str:
        '''
        def sortString(self, s: str) -> str:
    d={}
    
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    res=''
    keys = sorted(d.keys())
    
    while True:
        if len(res)==len(s):
            return res
        for i in keys + keys[::-1]:
            if d[i]>0:
                res+=i
                d[i]-=1
    return res
        
        '''
        result = []
        unique_letters = {}
        
        for letter in s: #make dictionary of unique letters and how many 
            if letter not in unique_letters:
                unique_letters[letter] = 1
            else:
                unique_letters[letter] += 1
        sorted_dict = sorted(unique_letters) #sort dictionary letters
        while len(result) != len(s): #until all the letters have been used...
            for key in sorted_dict + sorted_dict[::-1]: #append the forward+reversed letters
                if unique_letters[key] != 0:
                    result.append(key)
                    unique_letters[key] -= 1
        
            
        return "".join(result)
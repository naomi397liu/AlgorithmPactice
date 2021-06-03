class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        '''
        
        append sum arr[i:i+odd]
        
        
        
        '''
    
        
        def helper(arr, odds, length):
            if odds == []:
                return sum(arr)
            i = 0
            odd = odds.pop(0)
            while (i + odd) <= length:
                arr.append(sum(arr[i:i+odd]))
                i += 1
            return helper(arr, odds, length)
            
        odds = list(range(3, len(arr)+1, 2))
        length = len(arr)
        return helper(arr, odds, length)
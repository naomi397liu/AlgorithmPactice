def maximum69Number (self, num: int) -> int:
        '''
        to return the maximum we want the most left digit to be a nine, if 
        it's already a nine the change the next one. 
        
        
        
        '''
        num = str(num)
        nums = list(num)
        
        
        for i, n in enumerate(nums):
            if n == '6':
                nums[i] = '9'
                break
        return "".join(nums)
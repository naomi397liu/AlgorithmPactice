class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        just take the 2 largest numbers
        '''
        max1 = 0
        max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
           
        product = (max1-1)*(max2-1)
        return product
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        '''
        sort the array and then iterate through adding the front item to the back item by popping off the back item
        append the sums to a new array
        and return the max of that array
        
        '''
        sums = []
        nums.sort()
        for num in nums:
            sums.append(num+nums.pop())
        return max(sums)
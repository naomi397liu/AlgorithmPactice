class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        ex: [4,1,6,2,3]
        
        
        '''
        diff = 0 #keeps track of how much we add in total
     
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                change_by = nums[i] - nums[i+1] + 1
                diff += change_by
                nums[i+1] = nums[i] + 1
        return diff
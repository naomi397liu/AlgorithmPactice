class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        loop with a while k < k:
            - save to var pop()
            -insert(0, var)
        """
        if len(nums) < k:
            k = k % len(nums)
        new_nums = nums[len(nums)-k:]

        new_nums.extend(nums[:len(nums)-k])

        nums[:] = new_nums
        
        
        # i = 0
        # while i < k:
        #     popped = nums.pop()
        #     nums.insert(0,popped)
        #     i += 1
        # return nums
        

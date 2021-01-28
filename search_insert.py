def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if target <= nums[len(nums)-1] and target >= nums[0]:
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num < target and nums[i+1] > target:
                return i + 1
        
    elif target < nums[0]:
        return 0
    elif target > nums[len(nums)-1]:
        return len(nums)
    
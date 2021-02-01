def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #for an array with len 1, return its value
    #needs to iterate thru each value in the array and at a given value it needs to sum itself with the next, updating the value if it's a max sum
    #then we need to take the max sums for each value and return the max of those
    maxes = []
    if len(nums) == 1:
        return nums[0]
    for index, num in enumerate(nums):
        maximum = num
        
        for i in range(index + 1, len(nums)):
            num += nums[i] 
            if num > maximum: 
                maximum = num 
        maxes.append(maximum)
    return max(maxes)
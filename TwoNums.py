from random import randint
# class Solution(object):
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)-1):
            for j in range(1, len(nums)-1):
                if nums[j] + nums[i] == target:
                    return [i, j]
def numIdenticalPairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
#         we are given a list of integers
#         we need to check each integer against all the other integers after it for an element match
#         we could do this using a nested loop or we could create a hashmap for each element whose values are the elements that come after and check for matches that way
    
    matches = 0
    for i, num in enumerate(nums):
        for next_num in nums[i+1:]:
            if num == next_num:
                matches += 1
    return matches
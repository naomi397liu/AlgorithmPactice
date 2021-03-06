def decompressRLElist(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i = 1
    new_list = []
    for num in nums[::2]:
        new_list.extend(num * [nums[i]])
        i += 2
    return new_list
def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    #take in a list and val
    #iterate through the list and when val is found, remove it
        #add its index to a list
        #iterate thru nums and remove items corresponding with index - numbers removed so far
        #return length of nums
    indexes_to_remove = []
    num_removed = 0
    for i, num in enumerate(nums):
        if num == val:
            indexes_to_remove.append(i)
    for index in indexes_to_remove:
        nums.pop(index - num_removed)
        num_removed += 1
    return len(nums)
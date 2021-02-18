def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #take in list of nums
    #create a dictionary of those nums and if that key already exists,
    #remove the repeat item in the list
    #[0,0,1,1,1,2,2,3,3,4] [0,1,2,3,4,5,6,7,8,9,10]
    set_nums = set()
    indexes_to_remove = [] #[1,3,4,6,8]
    counter = 0
    
    for i, num in enumerate(nums): 
        if num not in set_nums:
            set_nums.add(num)
        else:
            indexes_to_remove.append(i)
    
    for index in indexes_to_remove: #[0,0,1,1,1,2,2,3,3,4]
        nums.pop(index - counter)   #[0,1,1,1,2,2,3,3,4]
        counter += 1                #
    
    return len(nums)
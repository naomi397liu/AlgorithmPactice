def shuffle(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    #will the len of yn always be the same as the len of xn? Assuming yes
    #the first y will be paired with the first x
    #the first y is at index n+1
    #iterate thru nums appending x and then y to a new list until reaching n
    
    def helper(nums, new_nums, n):
        if nums == []:
            return
        else:
            new_nums.append(nums.pop(0))
            new_nums.append(nums.pop(n-1))
            helper(nums, new_nums, n-1)
    
    new_nums = []
    helper(nums, [], n)
    return new_nums

def shuffle(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    #will the len of yn always be the same as the len of xn? Assuming yes
    #the first y will be paired with the first x
    #the first y is at index n+1
    #iterate thru nums appending x and then y to a new list until reaching n
    
    def helper(nums, i, n):
        if n == len(nums):
            return
        else:
            nums.insert(i, nums.pop(n))
            helper(nums, i+2, n+1)
    
    helper(nums, 1, n)
    return nums
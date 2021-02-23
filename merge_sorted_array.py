def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #start from the back and insert
        #solve it iterably then add recursion
        # once you find a spot where an item from nums2 fits, replace an item from nums 1 and then scoot the rest down an item
        
        #create a copy of nums 1 by slicing at index m 
        #iterate thru both starting from the back
        # whoever has the greater last value, pop it off and append it to the back
            #iterate thru og nums1 using range and rewrite in the values
    copy_nums = nums1[:m]
    
    for i in range(len(nums1)-1, -1, -1):
        if copy_nums == []:
            nums1[i] = nums2.pop()
        elif nums2 == []:
            nums1[i] = copy_nums.pop()
        elif nums2[-1] > copy_nums[-1]:
            nums1[i] = nums2.pop()
        elif copy_nums[-1] >= nums2[-1]:
            nums1[i] = copy_nums.pop()
    return nums1
                
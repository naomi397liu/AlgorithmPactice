def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
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
    
def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        def helper(nums1, nums2, copy_nums1, i):
            if nums2 == [] and copy_nums1 == []:
                return nums1
            elif copy_nums1 == []:
                nums1[i] = nums2.pop()
            elif nums2 == []:
                nums1[i] = copy_nums1.pop()
            elif nums2[-1] > copy_nums1[-1]:
                nums1[i] = nums2.pop()
            elif copy_nums1[-1] >= nums2[-1]:
                nums1[i] = copy_nums1.pop()
            helper(nums1, nums2, copy_nums1, i-1)
        
        copy_nums1 = nums1[:m]
        helper(nums1, nums2, copy_nums1, -1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        return a list of integers that are in nums1 and nums2
        
        plan of action:
        1-iterate thru nums1 if the num is also in nums2 then put it in a new array
        *how will we handle repeats? we will need to pop from nums2
        
        
        1-lets try to create 2 dictionaries for nums1 and nums2 such that the keys are the elements of the array and the values are the count of that num in the array
        2-iterate thru the keys of num1 and see if it's in nums2, if it is append it to a new array and reduce the count of each by 1
        3-after iterating check to see if any of the values of nums1 are non-zero if so, then check the count of the keys of those values in nums2 and append the key * min times it is seen
        
        make a dictionary of nums1 each with the val as a list with the count from nums1, then go thru nums2 and if it is a key in nums1, append its count, finally append the keys of nums1 the min number of times between the values
        
        '''
        result = []
        dic_nums1 = {}
        for num in nums1:
            if num in dic_nums1:
                dic_nums1[num][0] += 1
            else:
                dic_nums1[num] = [1,0]
        for num in nums2:
            if num in dic_nums1:
                dic_nums1[num][1] += 1
        for key in dic_nums1.keys():
            count = min(dic_nums1[key][0], dic_nums1[key][1])
            if count != 0:
                element = [key]*count
                result.extend(element)
        return result
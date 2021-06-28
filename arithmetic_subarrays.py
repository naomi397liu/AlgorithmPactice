class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        '''
        arithmetic sequence: goes up and down by the same number each time
        len(l) equals len(r)
        nums[i] is between [l[i], r[i]]
        
        return list of T and F
        as to whether each subarray for nums[i] can be arithmetic
        
        as you iterate thru nums, create the subarray
        then sort the subarray and iterate thru it until the difference isn't the same, then append False to the output array and move to the next
        
        '''
        result = []
        print(len(l))
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort()
            if len(subarray) <= 2:
                result.append(True)
            else:
                diff = abs(subarray[0] - subarray[1])
                for j in range(1, len(subarray)-1):
                    if abs(subarray[j]-subarray[j+1]) != diff:
                        result.append(False)
                        break
                    elif j+1 == len(subarray)-1:
                        result.append(True)
        return result
                    
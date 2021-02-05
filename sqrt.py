def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    #create a range of possible answers
    #As long as the start is less than the end, move either the start or the end to the mid pt
        # mid pt = end - start/2
        # if mid * mid is greater than x, then the new end is the mid pt
        # if mid * mid is less than x, then the new start is the mid point
        # if mid * mid is equal to x, then that is the answer
    
    end = x//2
    start = 1 
    while start <= end:
        mid = start + ((end - start) // 2)
        if x >= mid*mid and x < (mid+1) * (mid+1):
            return mid
        elif mid*mid > x:
            end = mid - 1
        elif mid*mid < x:
            start = mid + 1 
    
    return x
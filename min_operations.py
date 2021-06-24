class Solution:
    def minOperations(self, n: int) -> int:
        """
        n is the mean
        n//2 is the number of elements before the mean
        n//2 is also the arithmetic sum
        n//2 *n is the arithmetic sum after the operations
        
        def minOperations(self, n: int) -> int:
        a=[(2*i+1) for i in range(n)]
        print(a)
        mean=sum(a)//n
        summ=0
        for i in a:
            summ+=abs(mean-i)
        return summ//2
        
       - calculate the difference between the mean and each element and then divide it by 2 because we can do 2 operations per move 
        - bc we can do 2 operations per move, you could also simply sum the difference for either the first half or last half of elements
        
        """
        return n//2 * (n-n//2)
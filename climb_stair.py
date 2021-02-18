class Solution(object):
    memo = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            if n not in self.memo:
                self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memo[n]
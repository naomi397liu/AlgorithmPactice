def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        see an R, check if there's an L, if there is done!
        see an R check if there's an L, if not, remember how many rs and keep track of how many rs until you see an L, then keep adding Ls until there is as many Ls as Rs, done!
        """
        rs = 0
        ls = 0
        balanced = 0
        for i, letter in enumerate(s):
            if letter == 'R':
                rs += 1
            if letter == 'L':
                ls += 1
            if rs == ls:
                balanced += 1
                rs = 0
                ls = 0
        return balanced
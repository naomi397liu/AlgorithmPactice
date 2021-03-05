def numberOfSteps (self, num):
    """
    :type num: int
    :rtype: int
    """
    

    if num == 0:
        return 0
    if num % 2 == 0:
        num = num/2
    else:
        num -= 1
    return 1 + self.numberOfSteps(num) 
def subtractProductAndSum(self, n):
    """
    :type n: int
    :rtype: int
    """
    addition = 0
    multiplication = 1
    for digit in str(n):
        addition += int(digit)
        multiplication *= int(digit)
    return multiplication-addition
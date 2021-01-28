def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if x < 0:
        newNum = str(x)[::-1]
        newNum = newNum.rstrip('-')
        newNum = newNum.lstrip('0')
        newNum = '-' + newNum
        if not int(newNum) > -2**31:
            newNum = 0
    elif x > 0:
        newNum = str(x)[::-1]
        newNum = newNum.lstrip('0')
        if not int(newNum) <= (2**31)-1:
            newNum = 0
    else:
        newNum = 0
    return newNum


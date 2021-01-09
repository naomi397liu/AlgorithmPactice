def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if int(x) < 0 and int(x) <= (2**31-1):
            newNum = str(x)[::-1]
            newNum = newNum.rstrip('-')
            newNum = newNum.lstrip('0')
            newNum = '-' + newNum
    elif int(x) > 0 and int(x) >= -2**31:
        newNum = str(x)[::-1]
        newNum = newNum.lstrip('0')
    else:
        newNum = 0
    return newNum


def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n >= 1:
        new_num = "1"
    
    new_num_list = []
    for i, digit in enumerate(new_num):
        count = 1
        if i < len(new_num)-1 and digit == new_num[i+1]:
            count += 1
        new_num_list.extend([str(count), str(digit)])
        new_num = "".join(new_num_list)
        
    return countAndSay(n-1)
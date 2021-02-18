def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    prev = self.countAndSay(n-1)
    new_num_list = []
    i = 0
    while i < len(prev):
        count = 1
        while i < len(prev)-1 and prev[i] == prev[i+1]:
            count += 1
            i += 1
        new_num_list.extend([str(count), str(prev[i])])
        i += 1
    prev = "".join(new_num_list)
        
    return prev
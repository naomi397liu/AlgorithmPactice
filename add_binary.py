def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    #take in a binary string a and b and then output their sum
    # binary rules: 1 + 1 = 10, 0 + 1 = 1 
    # '110' '1011' -> 10001
    # loop thru the shortest str back to front
        # if the last value sum to > 1, change to 0 and add a 1 to the next value in the longer str
    #join back into a str and output
    #insert a 0 at the beginning of the shorter str until the strs are the same len
    while len(a) < len(b):
        a = '0' + a
    while len(b) < len(a):
        b = '0' + b
    b = list(b)
    a = list(a)
    for i in range(len(b)-1, -1, -1):
        b[i] = int(b[i]) + int(a[i])
        if int(b[i]) > 1 and i == 0:
            b[i] = int(b[i])%2
            b.insert(0, 1)
        elif int(b[i]) > 1:
            b[i] = int(b[i])%2
            b[i - 1] = int(b[i - 1]) + 1
    for i, num in enumerate(b):
        b[i] = str(num)
    
    return "".join(b)
def restoreString(self, s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    decode = {}
    sorted_word = []
    for i, index in enumerate(indices):
        decode[index] = s[i]
    
    for key in decode:
        sorted_word.append(decode[key])
        
    return "".join(sorted_word)
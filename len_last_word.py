def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    #take in a string, if we see a space we start counting after that space, but if we see another space, we reset our counting
    #if there are no words in the string, return 0
    #if theres only one word, we want to return its len
    
    #if there's a space in the string, split at the space and return the len of the last item [-1]
    
    
    words = s.split(" ")
    for i in range(len(words)-1,-1,-1):
        if len(words[i]) > 0:
            return len(words[i])
    return 0
    #if there's no space
    #what if there's a space in front of the str? or a space behind it?
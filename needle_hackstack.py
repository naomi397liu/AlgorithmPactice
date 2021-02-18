def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # hackstack = "aba" needle = "a" - will needle length always be longer than hackstack length?
    #we need to see if the needle is in the haystack
    # if it's not return -1
    # if it is then we need to return the index of the haystack char where the first character of the needle is seen
        #we need to watch out for partial matches 
    if needle in haystack:
        if len(needle) == 0 or len(haystack) == 1 or haystack == needle:
            return 0
        for i, char in enumerate(haystack):
                j = 0
                while haystack[i+j] == needle[j]:
                    j += 1
                    if j == len(needle):
                        return i
    else:
        return -1
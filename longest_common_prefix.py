def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    #if the list is empty, return ""
    if strs:
        if len(strs)==1:
            return strs[0]
        else:
            similar_letters = strs[0] #aba
            for str in strs: #""
                if str:
                    for i, letter in enumerate(similar_letters): #0,a
                        if (i == len(str)-1) and (letter == str[i]): #i=2 
                            similar_letters = similar_letters[:len(str)]
                            break
                        elif (letter != str[i]) and (i<len(str)): #i<3, 
                            similar_letters = similar_letters[:i]
                            break
                else:
                    similar_letters = []
                    break
            return "".join(similar_letters)
                    
                        
    else:
        return ""
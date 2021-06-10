import string
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        iterate thru the string backwards and append each character to as new list
        check to see if the new list is the same as the original
        
        import re

        string = "at what time?"
        match = re.sub("\s","!!!",string)
        print (match)
        """
        s = s.lower()
        adjusted = re.sub('[^a-z0-9]', "", s)
        j=0
        for i in range(len(adjusted)-1,-1,-1):
            if adjusted[i].lower() != adjusted[j].lower():
                    return False
            j += 1
        return True
        
#         backward = []
#         letters = string.ascii_lowercase
#         forward = []
#         for char in s:
#             if char.isdigit():
#                 forward.append(char)
#             if char.lower() in letters:
#                 forward.append(char.lower())
        
        
#         for i in range(len(forward)-1,-1,-1):
#             backward.append(forward[i])
#         return backward == forward
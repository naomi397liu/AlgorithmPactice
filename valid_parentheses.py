def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    #if s has odd number of symbols in it, return false
    #add open brackets to a stack and once a closed bracket is detected make sure it is the same type as what's on top of the stack else return false
    stack_open = []
    hash_brackets = {"(":")","[":"]","{":"}"}
    if len(s)%2 == 0:
        #if an open is detected, add it to the stack
        for bracket in s:
            if bracket in hash_brackets.keys():
                stack_open.append(bracket)
            elif bracket in hash_brackets.values() and stack_open:
                open_bracket = stack_open.pop()
                if hash_brackets[open_bracket] != bracket:
                    return False
            else:
                return False
        if stack_open:
            return False
        else:
            return True
    else:
        return False
                #if a closed is detected, make sure it matches the type of bracket at the top of the stack
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        '''
        return s excluding the outer most parentheses
        the first open partheneses is an outer 
        append it to a list outer
        all subsequent parentheses can be appended to a different list
        
        '''
        outer = []
        result = []
        for sym in s:
            if outer == [] and sym == "(":
                outer.append(sym)
            elif sym == "(":
                outer.append(sym)
                result.append(sym)
            elif len(outer) == 1 and sym == ")":
                outer.pop()
            elif sym == ")":
                outer.pop()
                result.append(sym)
            else:
                result.append(sym)
        return "".join(result)
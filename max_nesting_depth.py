class Solution:
    def maxDepth(self, s: str) -> int:
        """
        valid if empty or enclosed in parentheses or a single character
        nesting depth of empty or 1 character is 0
        nesting depth of () == 1 if there are multiple sets of (), the one with the max nesting depth is the overall nesting depth
        return nesting depth
        
        iterate through the string and keep track of the number of open parentheses
        when you encounter a closed parentheses save the number of open you have found to a variable max_parentheses
        As you find closed parentheses count down the number of current nesting depth, as you find open parentheses, count up current nesting depth
        Every time you come across a closed parenthese eval/update max parentheses
        
        
        """
        
        current_depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
            if char == ')':
                max_depth = max(max_depth, current_depth)
                current_depth -= 1
        return max_depth
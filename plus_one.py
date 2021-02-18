def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    #never an empty, positives only, no leading 0s to eliminate
    #list of digits represents an integer
    #output the next integer as a list of digits
    #edge cases: carrying the one
        #[9,9,9] -> [1,1,1,0]
        #[9] -> [1,0]
    #increment thru the digits from back to front
    #add 1 to the last digit and mod 10 the result
    #floor 10 the next value
    
    i = len(digits) - 1 
    digits[-1] += 1 
    while digits[i] > 9:
            digits[i] = digits[i] % 10
            if i == 0:
                digits.insert(0, 1)
                break
            i -= 1
            digits[i] += 1
            
    return digits
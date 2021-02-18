def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    #take in a str of digits and output all the letter combinations
    #dictionary - key: number, value = list of letters
    # iterate thru the digits and add combinations to seen
        # if not in seen add to output
        # ['a','b','c'] append d -> ['ad','bd','cd']
        # ' ' append e etc... -> ['ae','be','ce']
        #.extend -> ['ad','bd','cd','ae','be','ce'] etc

    num_to_letter = {
        '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
        '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
        '8':['t','u','v'], '9':['w','x','y','z']
                    }
    def function(i, prev_str):
        if len(prev_str) == len(digits):
            output.append(prev_str)
            return
        for new_letter in num_to_letter[digits[i]]: 
            new_str = prev_str + new_letter
            function(i+1, new_str)
    
    if digits == "":
        return []
    
    output = []
    i = 0
    function(i, "")
                
    return output
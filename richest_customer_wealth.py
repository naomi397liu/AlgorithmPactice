def maximumWealth(self, accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    # each row or each sublist represents a customer the sum of the ints in the list
    # represents a customers total wealth
    # we must find the total wealth of each customer and then return the max
    maximum = 0
    for row in accounts:
        if sum(row) > maximum:
            maximum = sum(row)
    return maximum

def maximumWealth(self, accounts):
    for i, row in enumerate(accounts):
            accounts[i] = sum(row)
    return max(accounts)

def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        
    def helper(accounts, i):
        if i == len(accounts):
            return
        accounts[i] = sum(accounts[i])
        helper(accounts, i+1)
    
    helper(accounts, 0)
    return max(accounts)
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
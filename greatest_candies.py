def kidsWithCandies(self, candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
#         how can a kid have the maximum number of candies if they take all extra candies for themselves
#         if that kid takes all the extra candies for themselves and still dont have the greatest number of candies then output false for that index
    greatest_num = []    
    for candy in candies:
        if candy + extraCandies >= max(candies):
            greatest_num.append(True)
        else:
            greatest_num.append(False)
    return greatest_num
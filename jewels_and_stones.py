def numJewelsInStones(self, jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    # how many characters in the string stones is also in the string jewels
    # one way we could do this is loop thru the characters in stones and check to see if it is in jewels but that would have a run time of O(n^2) because iterating thru the stones would be O(n) and then checking to see if it is in jewels would be O(n), but if we check to see if it is in jewels using a set or dicitionary then the runtime of that would be constant. Why? Because of hashing, the item is sorted in a specific place and if that item is in the set or dicitonary it will be in that one specific place or not. We simply check that one position as oppose to looking through all of our items to see if the one we want is among them. Think of searching for an item in a list or string like going thru your hamper to see what you wore 2 days ago, you would have to go thru the clothes that you have worn the past 2 days before you would get to the clothes you are looking for, but think of a set or dictionary like the clothes in your closet, they have a home and if they are not in the spot you keep them, then they must be dirty. Lets see that:
    
    jewel_stones = 0
    jewel_set = set(jewels)
    for char in stones:
        if char in jewel_set:
            jewel_stones += 1
    return jewel_stones
        
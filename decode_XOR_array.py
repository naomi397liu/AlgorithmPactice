def decode(self, encoded, first):
    """
    :type encoded: List[int]
    :type first: int
    :rtype: List[int]
    """
    arr = [first]
    for i in range(len(encoded)):
        arr.append(arr[i]^encoded[i])
    return arr
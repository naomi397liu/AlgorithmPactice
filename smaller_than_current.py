def smallerNumbersThanCurrent(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    output = []
    bucket = [0] * 101
    for num in nums:
        bucket[num] += 1
    for num in nums:
        output.append(sum(bucket[:num]))
    return output
    # // Given an array of positive numbers and a positive number ‘k,’ 
    # find the maximum sum of any contiguous subarray of size ‘k’.

    # // Input: [2, 1, 5, 1, 3, 2], k=3 
    # // Output: 9
    # // Explanation: Subarray with maximum sum is [5, 1, 3].

    # // Input: [2, 3, 4, 1, 5], k=2 
    # // Output: 7
    # // Explanation: Subarray with maximum sum is [3, 4].

def largest_sum(arr, k):
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)): 
        current_sum += arr[i] 
        if i >= k-1:
            max_sum = max(current_sum, max_sum)
            current_sum -= arr[i-k+1]
    return max_sum
print(largest_sum([4, 3, 4, 0, 5, 5], 3))
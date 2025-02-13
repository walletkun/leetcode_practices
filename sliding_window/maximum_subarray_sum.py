def maxSubarraySum(nums: list[int], k :int) -> int:
    maximumSum = sum(nums[:k])
    window_sum = maximumSum

    for right in range(k, len(nums) - 1):
        window_sum = window_sum - nums[right - k] + nums[right]
        maximumSum = max(maximumSum, window_sum)


    return maximumSum
    



# debug
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(maxSubarraySum(nums, 3))

# plan
'''
1. Sliding window technique is used
2. Initialize the sum calculation of the first k elements
3. During iteration for each subsequent index, update the window by subtracting the element that is leaving the window and adding in the new element 
4. Keep track of the maximum sum encountered
5. Return the maximum sum
'''
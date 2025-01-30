def maximumSubarray(nums: list[int]) -> int:
    maxSum = nums[0]
    res = nums[0]

    for i in range(1, len(nums)):
        maxSum = max(maxSum + nums[i], nums[i])
        res = max(res, maxSum)

    return res
        

# Debug
nums = [-2,1,-3,4,-1,2,1,-5,4]  
print(maximumSubarray(nums))

# Plan
'''
1. Keep track of the current maximum length inside the loop
2. Store a function scoped maximum length where each time we can achieve a better lenght of maximum summed subarray
3. Utilizing the concept of kadane's algorithm to compare the element at i - 1 with the current value at i or just check at i to see whihc value is larger
4. Return the maximum length
'''
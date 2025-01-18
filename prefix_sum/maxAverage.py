'''
Leetcode 643. Maximum Average Subarray I
Leetcode Link: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
Difficulty: Easy
Similar Problems: K Radius Subarray Averages
----------------------------
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''
# Prefix Sum solution
def findMaxAverage(nums: list[int], k: int) -> float:
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
        print(prefix)


    # Start calculating the max_average
    max_val = float('-inf')
    for i in range(k, n + 1):
        max_val = max(max_val, prefix[i] - prefix[i - k])
        print(max_val)
    return max_val / float(k)


nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))
        
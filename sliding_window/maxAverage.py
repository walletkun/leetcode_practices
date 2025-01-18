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

# Sliding window approach
def findMaxAverage(nums: list[int], k: int) -> float:
    # Initialze a window starting point 
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)


    return max_sum / float(k)


nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))
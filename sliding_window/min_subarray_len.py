'''
Leetcode 209. Minimum Size Subarray Sum
Leetcode Link: https://leetcode.com/problems/minimum-size-subarray-sum/
Difficulty: Medium
Similar problems: Minimum Window Substring, Maxmimum Length of Repeated Subarray
----------------------------

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

'''

def minSubarrayLen(nums:list[int], target: int,) -> int:

    left = 0
    min_length = float('inf')
    cur_sum = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
        while cur_sum >= target:
            # We only compare the min_length when shrinking happens
            min_length = min(min_length, right - left + 1)
            cur_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

nums = [1,1,1,1,1,1,1,1]
t = 11
print(minSubarrayLen(nums, t))

# Plan
'''
1. Simple sliding window problem
2. Where we will have 2 pointer left and right, right will be used to track down the expansion of the window
3. Left will be initialized for the starting point of the window
4. We will store a min_length variable for the minimum length of the window, using the right - left + 1 method
5. As well as the current sum will be localized within our window iteartion
6. We will track down if the current sum is less than our target we will expand the window by adding the current sum we initialzied to the nums[right] of the window
7. But if the current sum is greater than the target we will shrink the window by removing the left pointer value and incrementing the pointer
8. We will return the min length of the array
'''
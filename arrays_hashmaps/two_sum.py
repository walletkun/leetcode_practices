'''
Leetcode 1. Two Sum
Leetcode Link: https://leetcode.com/problems/two-sum/description/
Difficulty: Easy
Similar Problems:  3Sum, 4Sum, Two Sum II - Input Array is Sorted
----------------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''


def two_sum(nums: list[int], target: int) -> list[int]:
    complement_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_map:
            return [i, complement_map[complement]]

        complement_map[num] = i

    return [-1,-1]
# Debug
nums = [2, 7, 11, 15]
target = 9  
print(two_sum(nums, target))
# Plan
"""
1. Hashmap to store the complement between the target and the value in the input array
2. We enumerate through the nums to able to access the index
3. The value will be act as the index
4. The index because we then can see at which index we then will get the complement of the element is at
5. If the target is found, then we can return the value and the complement value in the map
""" 


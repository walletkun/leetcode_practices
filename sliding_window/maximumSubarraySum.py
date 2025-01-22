'''
Leetcode 2461. Maximum Sum of Distinct Subarrays With Length K
Leetcode Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
Difficulty: Medium
Similar Problems: Max Consecutive Ones, Optimal Partition of String
----------------------------
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
'''


def solution(nums: list[int], k: int) -> int:

    if len(set(nums)) < k: #If the set length does not build up to it then we can just return 0
        return 0
    seen = set()
    cur_sum = 0
    max_sum = 0
    
    left = 0
    for right in range(len(nums)):
        # If it's seen therefore not distinct we'll have to move the left pointer up
        while nums[right] in seen:
            seen.remove(nums[left])
            cur_sum -= nums[left]
            left += 1

        seen.add(nums[right])
        cur_sum += nums[right]

        # if the size of the window equals to k we'll compare with the max sum
        if right - left + 1 == k:
            max_sum = max(max_sum, cur_sum)

            seen.remove(nums[left])
            cur_sum -= nums[left]
            left += 1
            
    return max_sum


nums = [1,5,4,2,9,9,9]
k = 3
print(solution(nums, k))

'''
1. Use a set to maintain distinct elements in the window (this is the window)
2. Store the current sum in our window size
3. Only compare the size when k is met with formula right - left + 1 to maintain the size of the window
4. Still Shrink down the window size even after comparing because regardless of what happens after that the max_sum has been registered
5. Return the max sum
'''

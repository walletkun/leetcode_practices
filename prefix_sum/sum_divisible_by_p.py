'''
Leetcode 1590. Make Sum Divisible by P
Leetcode Link: https://leetcode.com/problems/make-sum-divisible-by-p/description/
Difficulty: Medium
Similar Problems: Subarray Sums Divisible by K, Find the Divisibility Array of a String
----------------------------

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
'''


def minSubarray(nums: list[int], p: int) -> int:
    total_sum = sum(nums)
    target = total_sum % p

    if target == 0:
        return 0

    remainder_map = {0 : -1}
    prefix_sum = 0
    min_length = len(nums)

    for i, num in enumerate(nums):
        prefix_sum += num % p
        cur_remainder = (prefix_sum - target) % p
        target_remainder = (cur_remainder - target + p ) % p

        if target_remainder in remainder_map:
            min_length = min(min_length, i - remainder_map[target_remainder])

        remainder_map[cur_remainder] = i


    return min_length if min_length < len(nums) else -1


# debug
nums = [3,1,4,2]
p = 6

print(minSubarray(nums, p))
# Plan
"""
1. 100% prefix sums straight off the bat
2. We will have to keep track of the occurrence we see of the remainder
3. Then we will have to keep track with the contiguous sums and finding it's remainder then locating it from our hashmap
4. Im assuming we have to check current sum each time we iterate over because of the tracking down each individual sums we sum up.
5. Keep track of the minimum lenght of the subarray, since we know that prefix sum is basically the sum between two slicing of the subarrays
6. Return the mininmum length
"""
    
        
    
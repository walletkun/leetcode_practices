''' 
Leetcode 1031. Maximum Sum of Two Non-Overlapping Subarrays
Leetcode Link: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
Difficulty: Medium
Similar problems: Maximum Sum of 3 Non-Overlapping Subarrays, Best Time to Buy and Sell Stock III

----------------------------

Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.

Constraints:
1 <= firstLen, secondLen <= 1000
2 <= firstLen + secondLen <= 1000
firstLen + secondLen <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


def maxSum_noOverlap(nums, firstLen, secondLen):
    def build_prefix_sum(nums):
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        return prefix_sum

    s = build_prefix_sum(nums)
    res = 0

    def maxSum(a, b):
        nonlocal res
        maxSum_a = 0
        for i in range(a + b, len(s)):
            maxSum_a = max(maxSum_a, s[i - b] - s[i - b - a])
            res = max(res, maxSum_a + s[i] - s[i - b])

    maxSum(firstLen, secondLen)
    maxSum(secondLen, firstLen)

    return res
    
    

def main():
    nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    firstLen = 1
    secondLen = 2

    output = maxSum_noOverlap(nums, firstLen, secondLen)
    print(output)
    
if __name__ == '__main__':
    main()
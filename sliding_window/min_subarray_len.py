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

def minSubarrayLen(target, nums):

    start = 0
    cur_sum = 0
    min_len = float("inf")

    for end in range(len(nums)):
        cur_sum += nums[end]
        while cur_sum >= target:
            min_len = min(min_len, end - start + 1)
            cur_sum -= nums[start]
            start += 1


    return min_len if min_len != float('inf') else 0


def main():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]

    output = minSubarrayLen(target, nums)
    print(output)

if __name__ == '__main__':
    main()
        
    

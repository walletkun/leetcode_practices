'''
Leetcode 560. Subarray Sum Equals K
Leetcode Link: https://leetcode.com/problems/subarray-sum-equals-k/
Difficulty: Medium
Similar problems: Two Sum, Continuous Subarray Sum
----------------------------

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

'''

def subarray_k(nums, k):
    
    prefix_sum = 0
    prefix_count = {0 : 1}
    count = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


def main():
    nums = [1, 2, 3]
    k = 3

    output = subarray_k(nums, k)

    print(output)

if __name__ == '__main__':
    main()
            
    

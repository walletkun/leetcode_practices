'''
Leetcode 238. Product of Array Except Self
Leetcode Link: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Similar problems: Trapping Rain Water, Maximum Product Array
----------------------------

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

def brute_array_except_self(nums):
    # Brute force approach which consists of n space
    n = len(nums)
    left_products = [0] * n
    right_products =  [0] * n
    left_products[0] = 1
    right_products[n - 1] = 1

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    res  = [0] * n

    for i in range(n):
        res[i] = left_products[i] * right_products[i]

    return res



def optimized_array_except_self(nums):
    n = len(nums)
    res = [0] * n

    left_products = 1
    for i in range(n):
        res[i] = left_products
        left_products *= nums[i]

    right_products = 1
    for i in range(n - 1, -1 ,-1):
        res[i] *= right_products
        right_products *= nums[i]

    return res


def main():
    nums = [-1, 1, 0, -3, 3]
    output_1 = brute_array_except_self(nums)
    print(output_1)

    output_2 = optimized_array_except_self(nums)
    print(output_2)
    

if __name__ == '__main__':
    main()

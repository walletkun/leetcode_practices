'''
Leetcode 228. Summary Ranges
Leetcode Link: https://leetcode.com/problems/summary-ranges/
Difficulty: Easy
Similar Problems: Missing Ranges
----------------------------
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
'''

def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []

    res = []
    start = nums[0]

    for i in range(1, len(nums) + 1):
        if i == len(nums) or nums[i] != nums[i - 1] + 1: # the sequence is broken or if we're at the last element:
            if start == nums[i - 1]:
                res.append(str(start))

            else:
                res.append(str(start) + "->" + str(nums[i - 1]))

            if i < len(nums):
                start = nums[i]
    return res


nums = [0,1,3,4,7]

print(summaryRanges(nums))

# Plan
"""
1. Consecutive sequence question
2. We first initilaize the starting point as nums[0] because that is the start point of the array
3. Initialize the result array as we need to return the ranges in terms of string
4. We will loop starting at 1 because our start pointer is already hovering the first index, and we're going to loop over until len(nums) + 1 because we need to consider the last element incase it's a single element
5. The condition where if we're at the last element or if the consecutive sequence is broken by nums[i] != nums[i - 1
] + 1
6. Then we'll check if the starting point equals to the previous that means it's a single value
7. Otherwise we can append with the nums[i- 1] that means there is a sequence
8. Checking if the start pointer is still within the boundary then we can update the start pointer as the index we're at right now.
9. Return the result array
"""     
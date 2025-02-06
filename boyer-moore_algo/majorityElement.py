'''
Leetcode 169. Majority Element
Leetcode Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Similar Problems: Majority Element II, Check if a number is Majority ELement in a Sorted List 
----------------------------
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

from collections import defaultdict
def hashMapSolution(nums: list[int]) -> int:

    freq = defaultdict(int)

    for num in nums:
        freq[num] += 1

    max_key = max(freq, key=freq.get)

    return max_key



# debug
nums = [3,2,3]

print(hashMapSolution(nums))

# plan
'''
1. Intuition use a frequency map to track down the most appeared value
2. Use max to locate down the max key value, since if two values have the same number of frequency
3. We will return the greater one
'''



# Boyer-moore algo 
def mooreSolution(nums: list[int]) -> int:
    candidate, count = None, 0


    for num in nums:
        if count == 0:
            candidate = num

        count += (1 if candidate == num else -1)

    return candidate


nums = [2,3,3]

print(mooreSolution(nums))
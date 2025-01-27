'''
Leetcode 992. Subarrays with K Different Integers
Leetcode Link: https://leetcode.com/problems/subarrays-with-k-different-integers/description/
Difficulty: Hard
Similar Problems: Longest Substring Without Repeating Characters, Longest Substring with At Most Two Distinct Characters
----------------------------

Descriptions of the Questions
'''


def subArraysKIntegers(nums: list[int], k) -> int:
    def atMostK(nums, k):
        # We will identify the frequency map
        frequency = {}
        maxLength = left = 0

        for right in range(len(nums)):
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1

            while len(frequency) > k:
                frequency[nums[left]] -= 1

                if frequency[nums[left]] == 0:
                    del frequency[nums[left]]

                left += 1

            maxLength += right - left + 1

        return maxLength

    result = atMostK(nums, k) - atMostK(nums, k - 1)

    return result

# debug
nums = [1,2,1,3,4]
k = 3
print(subArraysKIntegers(nums, k))

# Plan
"""
1. Similar to almost all k sliding window questions
2. We will use a helper function to help us determine how many subarrays can be formed with at most k dinstict values
3. But we also need to check the k - 1 values that are distinct because to make sure we don't miss any single k distinct values
4. Where in our helper function we will use a sliding window technique, where we will have a left pointer as our starting pointer and right pointer are our expanding pointer
5. Which we will also have a frequency map to keep track of the unique values we iterate over, then once our map is greater than our k amount, we will start shrinking the window
6. And instead of comparing like how we do in substrings, we will add the window size of our current window after each iteration because different from substring we're only looking at 1 singular max lenght substring, where as this is where we look up all different kinds of distinct subarrays
7. Then store the result with result = helper(nums, k) - helper(nums, k - 1) we're subtracting here because to reduce redundancy from the previous execution
8. Then return the result
"""
        
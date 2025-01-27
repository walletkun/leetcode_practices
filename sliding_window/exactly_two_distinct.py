'''
Lintcode 928 · Longest Substring with At Most Two Distinct Characters
Lintcode Link: https://www.lintcode.com/problem/928/
Difficulty: Medium
Similar Problems: Sliding Window Maximum, Longest Substring Without Repeating Characters
----------------------------

Description
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

Example 1:

Input: “eceba”
Output: 3

Explanation:
T is "ece" which its length is 3.

Example 2: 

Input: “aaa”
Output: 3

'''


def twoDistinct(s:str) -> int:
    if len(s) < 2:
        return len(s)

    left = maxLength = 0
    frequency = {}

    for right in range(len(s)):

        frequency[s[right]] = frequency.get(s[right], 0) + 1


        while len(frequency) > 2:
            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:
                del frequency[s[left]]

            left += 1


        maxLength = max(maxLength, right - left + 1)


    return maxLength

# Debug
s = "eceba"

print(twoDistinct(s))

# Plan
'''
1. We want to locate down the longest substring that contains exactly two distinct characters
2. Meaning if we have `eceba` we will have to return ece
3. We will be using sliding window technique to track down the maxlenght of the substring that contains the condition we're looking for
4. Instead of thinking of using a set, lets use a frequency map to track down the occurrences of the characters, then we will expand the window if we see new characters
5. Then we will just shrink the window by tracking the length of the frequecny map we had if it's greater than 2 therefore we will shrink the window
6. Compare the maxLength after the shrinking is complete
'''
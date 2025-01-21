'''
Leetcode 395. Longest Substring with At Least K Repeating Characters
Leetcode Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
Difficulty: Medium
Similar Problems: Longest Subsequence Repeated k Times, Number of Equal Count Substrings
----------------------------

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.


Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


from collections import defaultdict


def longestSubstring(s: str, k: int) -> int:
    if not s: return 0
    if k > len(s): return 0


    maxDistinct = len(set(s))
    maxLength = 0

    # We start looping the amount of the distinct characters that we can have in terms of the window
    for numDistinct in range(1, maxDistinct + 1): # start from 1 because it's impossible to even have 0 distinct characters
        charCount = defaultdict(int)
        valid_k = 0
        valid_distinct = 0
        left = 0


        for right in range(len(s)):
            charCount[s[right]] += 1
            if charCount[s[right]] == 1: # If it's 1 that means it's a new character we're visiting
                valid_distinct += 1

            if charCount[s[right]] == k: # if it's equal to k that means we're completing the validation of k amount of occurrence
                valid_k += 1


            while valid_distinct > numDistinct: # That means our current valid distinct amount of characters exceeded the current available distinct we're looping through
                if charCount[s[left]] == k: # It's valid but we have to that out that because it's exceeded the validation window size
                    valid_k -= 1
                charCount[s[left]] -= 1
                if charCount[s[left]] == 0:
                    valid_distinct -= 1
                    
                left += 1

            if valid_k == numDistinct:
                maxLength = max(maxLength, right - left + 1)


    return maxLength

            
s = 'aaabb'
k = 2

print(longestSubstring(s,k))


'''
1. Sliding window is a must
2. Two pointers to track down the window size
3. Must Remember to track down the maximum distinct characters in our string
4. looking at it we definetly need to use a frequency counter
5. Because we need to check if the occurrence of the characters met the condition of k amount
6. But also we have to utitlize the trackign condition of the values, so if the current value we met is at least k amount, then we have to keep track of that with a variable, then using that variable to track if the value is within the bound.
7. We will then return the length of the window, which is by doing right - left + 1 to get the max_legnth
8. Reutrn that
'''
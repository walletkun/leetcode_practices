'''
Leetcode 76. Minimum Window Substring
Leetcode Link: https://leetcode.com/problems/minimum-window-substring/description/
Difficulty: Hard
Similar Problems: Substring with Concatenation of All Words, Minimum Size Subarray Sum, Sliding Window Maximum
----------------------------

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

from collections import Counter
def minWindow(s: str, t: str) -> str:

    if not s or not t:
        return ""
    window = Counter()
    t_map = Counter(t)
    left = 0
    have, need = 0, len(t_map)
    res, res_len = [-1,-1], float("inf")

    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        if char in t_map and window[char] == t_map[char]:
            have += 1

        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            left_char = s[left]
            window[left_char] -= 1

            if left_char in t_map and window[left_char] < t_map[left_char]:
                have -= 1

            left += 1

    l,r = res
    return s[l: r + 1] if res_len != float("inf") else ""
        


# Debug
s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))

# Plan

'''
1. Using sliding window technique to solve this problem
2. Since this question is asking for the minimum window substring aka the minimum size of the window
3. Our condition is to only fulfill the t string 
4. So in terms of the frequecny map, we'll have 2 variable 1 I will call it have, and 1 will be called need
5. Where need will be the length of the t_map, and have is how much we're currently fulfilled with
6. I will also initialize a result to store the variables left and right to accumulate for the slciing later, and result length to store the length of the current window size we have, to keep it the minimum possible length
7. Inside the iteration of the loop, we will have the window_map to accumulate the current character, and we're going to check if the character is in our t_map and if the window_map[character] == t_map[character] because we want to makesure that it's frequency matches, where since we're looking for the character frequency of t_map
8. Then we only start shrinking if our have equals to our need. Because that means we have successfully accumulated all the sequences we need but that's only after we shrink the window, because we can have the substring to be satisfy if the map contains it.
9. Return by unpacking the res with 2 indicies then slice return of the first string
'''
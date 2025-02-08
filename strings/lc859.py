'''
Leetcode 859. Buddy String
Leetcode Link: https://leetcode.com/problems/buddy-strings/
Difficulty: Easy
Similar Problems: lc1790
----------------------------

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
'''


def buddyStrings(s: str, goal: str):
    if len(s) != len(goal):
        return False


    if s == goal:
        return len(set(s)) < len(s)


    indices = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            indices.append(i)


    return len(indices) == 2 and s[indices[0]] == goal[indices[1]] and s[indices[1]] == goal[indices[0]]




# debug
s = 'aba'
goal = 'baa'

print(buddyStrings(s,goal))

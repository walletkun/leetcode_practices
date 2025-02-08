'''
Leetcode 1790. Check If One String Swap Make String Equal
Leetcode Link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
Difficulty: Easy
Similar Problems: Buddy Strings
----------------------------
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
'''


def areAlmostEqual(s1: str, s2: str):
    indexes = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            indexes.append(i)

        if len(indexes) > 2:
            return False

    if len(indexes) == 2:
        i, j = indexes

        if s1[i] == s2[j] and s1[j] == s2[i]:
            return True
        
    return len(indexes) == 0


# Debug
s1 = "anbk"
s2 = "bank"

print(areAlmostEqual(s1,s2))

# Plan
"""
1. Use a indexing array method
2. Where the index array will keep track of the indice that we're seeing two different characters
3. Which the problem specifically tells us that to at most have 1 string swap on the string
4. Therefore if the appending of the indexes exceeds 2 that means we can break the loop as false.
5. Otherwise if the length of the indexing array is exactly length of 2 that means a swap can be make, since it's a pair where at index i we can find it different, and index j we also find it different
6. Then we use unpacking and check if it's possible like if s[i] == t[j] and s[j] == t[i] then it's true
7. Otherwise if length of the index array is 0 that means that string was already equal.
"""
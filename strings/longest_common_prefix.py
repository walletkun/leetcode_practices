'''
Leetcode 14. Longest Common Prefix
Leetcode Link: https://leetcode.com/problems/longest-common-prefix/description/
Difficulty: Easy
Similar Problems: Smallest Missing Integer Greater Than Sequential Prefix Sum
----------------------------

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs: list[str]) -> str:
    prefix = strs[0]
    pref_len = len(prefix)

    for s in strs[1:]:
        while prefix != s[0:pref_len]:
            pref_len -= 1
            if pref_len == 0:
                return ""


            prefix = prefix[0:pref_len]

    return prefix


# Debug
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# plan
"""
1. We will first initialize the prefix of the string in the str first element
2. intialzie the length of that prefix variable
3. Then we're going to iterate over the string start from the second value because we've initialized the variable being the first string
4. Then we're going to loop through each string we're currently checking it's sliced value from 0 to the prefix length that we have and asking if it's equal
5. If it's not we're decrease our prefix length, and since it's in a while loop. It will not stop looping until we get what we needed
6. Then we will compare the prefix after we locate down the prefix we found
7. If the prefix length falls to 0 we will return an empty string because it's not a prefix of our value
8. Otherwise it will continue looping until the prefix is found then we return the prefix
"""
        
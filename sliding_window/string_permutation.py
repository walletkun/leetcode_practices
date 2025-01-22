'''
Leetcode 567. Permutation in String
Leetcode Link: https://leetcode.com/problems/permutation-in-string/description/
Difficulty: Medium
Similar Problems: Minimum Window Substring, Find All Anagrams in a String
----------------------------
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    s1_counter = Counter(s1)
    window_size = len(s1)
    s2_counter = Counter(s2[:window_size]) # Fixed window size, start counting all the way till the window length

    # If the counter already satisfy then we can just return True 
    if s1_counter == s2_counter:
        return True

    for right in range(window_size, len(s2)):
        s2_counter[s2[right]] += 1
        # Shifting the window
        left_char = s2[right - window_size]
        s2_counter[left_char] -= 1 # since we moved it therefore the first character can be removed
        if s2_counter[left_char] == 0:
            del s2_counter[left_char] # If the value is 0 we then can remove that from our map

        if s1_counter == s2_counter:
            return True

    return False


s1 = "ab"
s2 = "eidboabooo"
print(checkInclusion(s1, s2))


# Plan
'''
1. Sliding window technique
2. It's also a fixed sized sliding window
3. We're going to use the frequency counter of the character appearence of the first string and the second string but from the window size which is the len of the first string
4. It's a fixed size because shown in example 2, ba showed up but theres a character o in between the occurence therefore it's false
5. Going to break out after the permutation is found and return true
6. Return false is it's not found
'''
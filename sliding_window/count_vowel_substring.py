'''
Leetcode 2062. Count Vowel Substrings of a String
Leetcode Link: https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
Difficulty: Easy
Similar Problems:  Number of Matching Subsequences, Subarrays with K Different Integers
----------------------------

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

 

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
'''


def countVowelSubstrings(word: str) -> int:
    if len(word) < 5:
        return 0
    left = result = 0
    vowels = set("aeiou")

    while left < len(word):
        if word[left] not in vowels:
            left += 1
            continue

        vowel_set = set()

        for right in range(left, len(word)):
            if word[right] not in vowels:
                break

            vowel_set.add(word[right])

            if len(vowel_set) == 5:
                result += 1

        left += 1
        
    return result

# debug
word = "aeiouu"
print(countVowelSubstrings(word))

# plan
"""
1. We will use a pure sliding window approach
2. Where we will start iterating from the left pointer
3. And within that pointer we will build a right pointer in which that right pointer will act as a exapdning the window
4. If the right pointer we're currently in is in the vowels set that means we can continue expanding it, but if it's not we will have to result and continue building
5. We will also use a set inside to track for vowel validity making sure all vowels are counted down
6. Return the total amount of strings built from the window
"""



                

        
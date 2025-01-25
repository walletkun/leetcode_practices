'''
Leetcode 1657. Determine if Two Strings Are Close
Leetcode Link: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Similar Problems: Buddy Strings, Minimum Swaps to Make Strings Equal
----------------------------

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
'''


def closeStrings(word1:str, word2:str) -> bool:
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False

    # Using a hashmap solution
    freq1 = {}
    freq2 = {}

    for word in word1:
        freq1[word] = freq1.get(word, 0) + 1

    for word in word2:
        freq2[word] = freq2.get(word, 0) + 1


    return sorted(list(freq1.values())) == sorted(list(freq2.values()))


# Debug
word1 = "abc"
word2 = "bca"

print(closeStrings(word1, word2))

# 2 solutions
'''
Use a hashmap or we can use a list for storing the counter of the existing character then sort that list, if they are equal then we reutrn equal
Using a hashmap requires us to counter through each string and store their frequency then return the values list
'''


'''
Leetcode Daily 2559. Count Vowel Strings in Ranges
Leetcode Link: https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-02
Difficulty: Medium
Similar problems: 345. Reverse Vowels of a String, 1641. Count Sorted Vowel Strings
----------------------------

Given an array of strings 'words' and queries, count number of strings in the 
queries that have both starting and ending characters as vowels.
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
 
'''
def countVowels(words, queries):
    # Get the vowels of in terms of sets
    vowels = {'a','e','i','o','u'}

    # Use a helper function to determine if the string starts with a vowel and ends with a vowel
    def is_vowel_string(word):
        return word[0] in vowels and word[-1] in vowels

    # Compute if the words are valid
    valid = [is_vowel_string(word) for word in words] # Checking if all the word are valid (Start with vowel and end with vowel)
    # print(valid) <- debug line

    #Prefix sum array
    n = len(valid)
    prefix = [0] * n # [0, 0 ,0, 0, 0] <- Using example 1 this is what prefix looks like
    prefix[0] = 1 if valid[0] else 0 # To start off the prefix we'll have to start with 1 at the beginning to prevent value error
    # print(prefix) <- debug line
    # Build our prefix array
    for i in range(1, n): # Start at 1 since we built 1 at the 0'th index 
        prefix[i] = prefix[i - 1] + (1 if valid[i] else 0) # We're going to add 1 if the word is valid else we add 0 which is basically nothing

    # Build our result array
    res = []
    for li, ri in queries: # Going to loop through the queries [li, ri] 
        if li == 0:
            res.append(prefix[ri])

        else:
            res.append(prefix[ri] - prefix[li - 1]) # Otherwise we're going to subtract prefix[li - 1] from prefix[ri] because ri is always going to be bigger than li since it's ending slice


    return res

# Test run
def main():
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]] 

    output = countVowels(words, queries) #Expected output: [2,3,0]
    print(output)

if __name__ == '__main__':
    main()
        

    
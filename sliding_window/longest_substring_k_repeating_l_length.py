from collections import defaultdict

def solution(s: str, k: int, l: int) -> int:
    maxLength = 0

    # Ensure we only process windows with exactly l distinct characters
    for numDistinct in range(l, l + 1):
        charCount = defaultdict(int)
        valid_k = 0
        valid_distinct = 0
        left = 0  # Starting point of the window

        for right in range(len(s)):
            # Expand the window
            charCount[s[right]] += 1
            if charCount[s[right]] == 1:  # First appearance of the character
                valid_distinct += 1
            if charCount[s[right]] == k:  # Character meets or exceeds frequency k
                valid_k += 1
            # Shrink the window if there are too many distinct characters
            while valid_distinct > numDistinct:
                if charCount[s[left]] == k:  # If the character being removed met k
                    valid_k -= 1

                charCount[s[left]] -= 1
                if charCount[s[left]] == 0:  # Completely remove the character
                    valid_distinct -= 1
                left += 1

            print(f"Window: {s[left:right+1]}, valid_distinct: {valid_distinct}, valid_k: {valid_k}, maxLength: {maxLength}")

            # Update maxLength if the window is valid
            if (valid_distinct == l) and (valid_k == valid_distinct):
                #print(valid_distinct)
                maxLength = max(maxLength, right - left + 1)


    return maxLength
                



s = "aaabbccc"
k = 3
l = 2

print(solution(s, k, l))



# Plan
'''
1. Do the same thing except we need to count for the l as well, where the length must not exceed the limitation distinct character
2. Instead of iterating from 1, we loop from l and keep adding in values, that equals up to l
3. If the window's distinct characters exceeded the l, length then we will start shrinking the window as we delete the character out from our map
4. Initialize the max length, and for the max length we only compare it when the distinctCharacters in the window is the same as the length of l and the valid k is the same as k
5. Return the max length
'''
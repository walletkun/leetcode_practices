from collections import defaultdict

def solution(s: str, k: int) -> int:
    charCount = defaultdict(int)
    maxLength = 0
    left = 0


    for right in range(len(s)):
        # populate the hashmap since its a default dict we don't have to worry about initializign a null key
        charCount[s[right]] += 1

        # Shrink the window if the number of distinct character exceeds k
        while len(charCount) > k:
            # Decrement the count of the character
            charCount[s[left]] -= 1
            # Remove the character occurence of the character becomes 0
            if charCount[s[left]] == 0:
                del charCount[s[left]]

            # Shrink the window by incrementing the pointer to the right
            left += 1


        # Update the max length
        maxLength = max(maxLength, right - left + 1)

    return maxLength

                
        

s = "eceba"
k = 2

print(solution(s, k))


'''
1. Going to use two pointer left and right, left( to track the starting of the window) and right (to track the end of the window)
2. Use a hashmap to track the count of the characters in the current window
3. Track down the maximum length of the valid substring
4. Expand the window to include the next character in the window
5. Shrink if the number of distinct characters exceeds k
6. Remove the left character from the window by decrementing the count in the hashmap
7. If the counter becomes 0 we remove it from the map
8. Increment the left to imitate shrinking the window
9. Update the max length
'''
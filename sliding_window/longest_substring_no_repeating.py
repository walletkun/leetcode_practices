# def solution(s: str) -> int:
#     max_len = 0
#     left = 0
#     window = set()
#     for right in range(len(s)):
#         while s[right] in window:
#             window.remove(s[left])
#             left += 1

#         window.add(s[right])

#         max_len = max(max_len, right - left + 1)


#     return max_len


# s = "azbasr"
# print(solution(s))

# Use a hashmap apporach to imitate a sliding window
def map_solution(s: str) -> int:
    char_map = {}
    left = 0
    maxLength = 0

    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1

        char_map[s[right]] = right

        maxLength = max(maxLength, right - left + 1)

    return maxLength

s = "abcabcbb"
print(map_solution(s))

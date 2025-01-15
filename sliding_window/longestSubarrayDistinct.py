'''
Custom Questions will not come with templates
'''


def solution(nums):
    seen = set(nums)
    max_length = 0
    
    for num in nums:
        if num - 1 not in seen: # To find the starting point
            cur_num = num # if not this is the starting point
            length = 1

            while cur_num + 1 in seen: # Then we want to increment the num by 1 to start locating the rest of the num
                length += 1
                cur_num += 1

            max_length = max(max_length, length)


    return max_length
                

nums = [1, 2, 3, 1, 2, 3, 4, 5]
print(solution(nums))


'''
Literally the question of of (forgot)
'''
# Can generate even further with this distinct question with K elements, and output is the distinct elements
def alternative_solution(nums:list[int], k:int) -> list[int]:
    seen = set(nums)
    res = []
    for num in seen:
        if num - 1 not in seen:
            cur_num = num
            res = [cur_num] # Keep track with the starting point of the sequence
            while cur_num + 1 in seen:
                cur_num += 1
                res.append(cur_num)

                if len(res) == k:
                    return res

    return res

nums = [1, 2, 3, 1, 2, 3, 4, 5]
k = 5
print(alternative_solution(nums, k))
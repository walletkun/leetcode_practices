def two_sum(nums, target):
    h_map = {}

    for idx, num in enumerate(nums):
        difference = target - num
        if difference in h_map:
            return [h_map[difference], idx] # [0, 1]

        h_map[num] = idx #{2 : 0, }

    return [-1, -1]


nums = [15,20, 50 ,0]  
target = 15

print(two_sum(nums, target)) # [0, 3]



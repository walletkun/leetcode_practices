def two_distinct_pairs(nums, target):
    nums.sort()
    closest_sum = float('inf')
    closest_pair = []
    l = 0
    r = len(nums) - 1
    
    while l < r:
        cur_sum = nums[l] + nums[r]

        diff = abs(target - cur_sum)

        if diff < abs(target - closest_sum) and len(closest_pair) < 2:
            closest_sum = cur_sum
            closest_pair.append((nums[l], nums[r]))
        elif diff == abs(target - closest_sum):
            closest_pair.append([nums[l], nums[r]])
            
        if cur_sum < target:
            l += 1

        else:
            r -= 1


    return closest_pair[:2]

nums = [10, 22, 28, 29, 30, 40]
target = 54

print(two_distinct_pairs(nums, target))
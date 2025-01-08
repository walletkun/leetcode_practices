def closest_pair(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    closest_sum = float('inf')
    closest_pair = []

    while l < r :
        cur_sum = nums[l] + nums[r]
        diff = abs(target - cur_sum)

        if diff < abs(target - closest_sum):
            closest_sum = cur_sum
            closest_pair = [nums[l], nums[r]]

        if cur_sum < target:
            l += 1

        else:
            r -= 1

    return closest_pair


nums = [10, 22, 28, 29, 30, 40]
target = 54

print(closest_pair(nums, target))
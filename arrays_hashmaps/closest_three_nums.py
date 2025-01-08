def closest_three_number(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i -1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            cur_sum = nums[i] + nums[l] + nums[r]

            if abs(target - cur_sum) < abs(target - closest_sum):
                closest_sum = cur_sum

            if cur_sum == target:
                return cur_sum
                
            if cur_sum < target:
                l += 1
                
            else:
                r -= 1


    return closest_sum

nums = [-1, 1, 1, 4]
target = 7
print(closest_three_number(nums, target))

        

    
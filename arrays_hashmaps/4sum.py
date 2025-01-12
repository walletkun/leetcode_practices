def fourSum(nums,target):
    if len(nums) < 4:
        return []
    
    nums.sort()
    res = []

    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(n - 3):
            if j > i + 1 and nums[j] ==  nums[j - 1]:
                continue

            l, r = j + 1 , n - 1

            while l < r:

                cur_sum = nums[i] + nums[j] + nums[l] + nums[r]

                if cur_sum == target:
                    res.append([nums[i] , nums[j] , nums[l] , nums[r]])

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r += 1

                elif cur_sum < target:
                    l += 1

                else:
                    r -= 1

    return res


nums = [0, 0, 0, 0]
target = 0
print(fourSum(nums, target))

def twoSumDuplicated(nums: list[int], target: int) -> list[int]:

    left , right = 0, len(nums) -1
    res = []

    while left < right:


        cur_sum = nums[left] + nums[right]

        if cur_sum == target:
            res.append([left, right])
            left += 1
            right -= 1

        elif cur_sum < target:
            left += 1

        else:
            right -= 1


    return res if res else [-1, -1]


nums = [1,2,2,3]
target = 4
print(twoSumDuplicated(nums, target))

'''
1. Use two pointer, and we're going to skip the duplicated value if it was found
2. Then compare the current sum with the target, if the same return the pointers
3. Otherwise continue and increment the left pointer if the current sum is less than the target
4. Decrement the right pointer if the current sum is greater than the targer
5. If it doesnt exist return -1,-1
'''
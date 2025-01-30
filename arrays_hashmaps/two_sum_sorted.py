def sortedTwoSum(nums: list[int], target : int) -> list[int]:

    if sum(nums) < target:
        return [-1, -1]

    
    left, right = 0, len(nums) - 1

    while left < right:
            
        cur_sum = nums[left] + nums[right]
            
        if cur_sum == target:
            return [left, right]

        elif cur_sum < target:
            left += 1

        else:
            right -= 1


    return [-1,-1]


# debug
nums = [2, 7, 11, 15]
target = 9

print(sortedTwoSum(nums, target))


'''
1. utilize two pointers approach where we will have a pointer at the start and a point at the end
2. calcualte that sum then compare with the target
3. If it equals to the target we can return the pointers
4. Otherwise if the sum is less than the target we can move the left pointer
5. Else we move the right pointer
6. If no solution were found return [-1,-1]
'''
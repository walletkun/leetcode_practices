def solution(nums) -> list[int]:
    # We know that it's sorted therefore we don't need to sort it again
    # Utilize the formula of checking for the closest => abs(cur_sum) < abs(closest_sum)
    closest_sum = float('inf')
    res = []

    # Use two pointers to dynamically check from front of the array and the back to stay within bound without missing values
    left , right = 0, len(nums) - 1

    # Start two pointer iteration
    while left < right:
        cur_sum = nums[left] + nums[right]
        target = 0

        if abs(cur_sum) < abs(closest_sum):
            closest_sum = cur_sum
            res=[nums[left], nums[right]]


        if cur_sum < target:
            left += 1

        else:
            right -= 1

    
    return res

nums = [-10, -5, 1, 4, 8, 20]

print(solution(nums))
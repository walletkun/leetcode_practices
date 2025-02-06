'''
Max difference of the input array
'''

def maxDifference(nums: list[int]) -> int:
    min_price = nums[0]
    max_difference = 0

    for i in range(1, len(nums)):
        min_price = min(min_price, nums[i])
        max_difference = max(max_difference, abs(nums[i] - min_price))

    return max_difference
            

# debug
nums = [9,1,3,7,2,8]
print(maxDifference(nums))


# plan
'''
1. We need to have a variable to track down the maximum difference
2. Keep on tracking and iterating over the input array
3. Calcualte the difference in the interation
4. Compare for the maximum differences
5. Return that
'''
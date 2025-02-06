'''
Easy Alternative of Product of Array except self
'''

def productExceptSelf(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    res[0] = nums[0]

    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]

    return res

# Debug
nums = [1,2,3,4]
print(productExceptSelf(nums)) # [1,1,2,6]

# Plan
'''
1. First we have to initlaize the result array with all 0's using pythonic [0] * len(nums)
2. Initalize a for loop to accumulate the product of our result array and the input array
3. We iterate starting from 1 since we only need the product from l: r, since r is exclusive therefore we're computed the product from l : r.
4. This is the prefix sum approach
5. Return the result array
'''
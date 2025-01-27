def sumsEqualK(nums: list[int], k: int) -> int:

    prefix_sum = 0
    count = 0
    hashmap = {0 : 1} # Initialize with prefix sum 0

    for num in nums:
        # Update the prefix sums
        prefix_sum += num

        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count

# Debug
nums = [1,2,3]
k = 3
print(sumsEqualK(nums, k))

# Plan
'''
1. Prefix sums question
2. Given from gpt, that we will be using hashmap to store the frequency of prefix sums seen so far
3. And we're going to check if prefix[i] - k exists in our map which this indicates our subarray sum of k
4. Then we can return the length of the subarrays that will sum up to k.\
'''
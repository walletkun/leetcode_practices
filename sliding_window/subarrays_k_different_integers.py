

def subArraysKIntegers(nums: list[int], k) -> int:

    def atMostK(nums, k):
        # We will identify the frequency map
        frequency = {}
        maxLength = left = 0

        for right in range(len(nums)):
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1

            while len(frequency) > k:
                frequency[nums[left]] -= 1

                if frequency[nums[left]] == 0:
                    del frequency[nums[left]]

                left += 1

            maxLength += right - left + 1

        return maxLength

    result = atMostK(nums, k) - atMostK(nums, k - 1)

    return result

# debug
nums = [1,2,1,3,4]
k = 3
print(subArraysKIntegers(nums, k))

# Plan
'''
1. We will need to have a helper function to help us how many result sub arrays we can form from our array
2. Which by utilizing the formula which is subarray with exactly k = (subarray with at most k) - (subarrays with at most k - 1)
3. Plan for the helper function we will need to use a sliding technique to identify when we will shrink the window and when we will expand the window
4. We will use a hashmap to count the occurrence of how many distinct values we can have, since the question can have at most K we then can have less than k.
5. Therefore we will utilize the formula subarray with exactly k = (subarray with at most k) - (subarrays with at most k - 1)
4. Then we will store the formula in our result then return the result
'''
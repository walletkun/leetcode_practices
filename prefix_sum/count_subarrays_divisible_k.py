def countSubarraysEqualsK(nums: list[int], k: int) -> int:
    count = 0
    prefix_map = {0 : 1} 
    prefix_sums = 0

    for num in nums:
        prefix_sums += num

        remainder = (prefix_sums%k + k) % k
        if remainder in prefix_map:
            count += prefix_map[remainder]

        prefix_map[remainder] = prefix_map.get(remainder, 0) + 1


    return count


# debug:
nums = [4, 5, 0, -2, -3, 1]
k = 5

print(countSubarraysEqualsK(nums, k))
# Plan
'''
1. Utilize hashmap to keep count of the key value, where the key is going to be the remainder and the value is just going to be deafult 1 
2. We will store in a prefix sum to keep track of the contiguous running sum
3. We will also utilize a counter variable to keep track of the counter (our subarray count)
4. We will iterate through the nums array and we will update the current prefix_sum with the current running value
5. Check if the remainder with (prefix_sum%k + k) % k exists in our map. The reason being not using straight up prefix[j]%k == prefix[i - 1]%k is because with % we will get negative results
6. Therefore with (prefix_sum%k + k) % k  we will get all positive values without missing the negative part
7. Return the counter
'''
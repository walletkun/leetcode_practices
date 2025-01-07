def first_unique(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num in nums:
        if freq[num] == 1:
            return num

    return -1

nums = [7,7,7,7]
print(first_unique(nums))
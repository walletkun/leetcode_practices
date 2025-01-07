def first_repeated(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > 1:
            return num

    return -1


nums = [10, 5, 3, 4, 3, 5, 6]
print(first_repeated(nums))
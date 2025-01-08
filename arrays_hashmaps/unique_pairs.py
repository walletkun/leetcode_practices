def unique_pairs(nums, target):
    h = set()
    s = set()

    for num in nums:
        diff = target - num
        if diff in h:
            s.add((min(num, diff), max(num, diff)))

        h.add(num)

    return list(s)
       
        


nums = [2, 7, 11, 15, -2, 8, 7]
target = 9

print(unique_pairs(nums, target))
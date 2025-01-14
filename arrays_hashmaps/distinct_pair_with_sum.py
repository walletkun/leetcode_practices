def solution(nums: list[int], target: int) -> int:
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((complement, num)))
            if pair not in pairs:
                pairs.add(pair)

        seen.add(num)

    return len(pairs)



'''
1. Utilize a hashmap to track seen (use a hashset instead)
2. Initialize a counter if it does exist, then increment the counter
3. Return counter
'''


nums = [1,5, 7, -1, 5 ]
target = 6

print(solution(nums, target))
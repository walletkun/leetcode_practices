'''
Leetcode 
Leetcode Link: <Link> or Any Link: <Link>
Difficulty: Difficulty
Similar Problems: 
----------------------------

Descriptions of the Questions
'''

def solution(nums: list[int]):
    last_not_zero = 0

    for num in nums:
        if num != 0:
            nums[last_not_zero] = num
            last_not_zero += 1

        
    for i in range(last_not_zero, len(nums)):
        nums[i] = 0


nums = [1,0,3,0,12] # Expected: [1,3,12,0,0]
solution(nums)
print(nums)

    
    
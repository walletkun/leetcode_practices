'''
Leetcode 641. Missing Ranges
Leetcode Link: https://www.lintcode.com/problem/641/
Difficulty: Medium
Similar Problems: lc228
----------------------------
Description
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], 
return its missing ranges.

Example
Example 1

Input:
nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
Output:
["2", "4->49", "51->74", "76->99"]
Explanation:
in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]
Example 2

Input:
nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
Output:
["4->6"]
Explanation:
in range[0,7],the missing range include range[4,6]
'''


def missingRanges(nums: list[int], lower: int, upper: int) -> list[str]:
    prev = lower - 1
    curr = 0

    res = []


    for i in range(len(nums) + 1):
        if i < len(nums):
            curr = nums[i]
        else:
            curr = upper + 1


        if prev + 1 < curr:

            if prev + 1 == curr - 1:
                res.append(str(prev + 1))

            else:
                res.append(f"{prev + 1}->{curr - 1}")

        prev = curr


    return res


# Debug
nums = [0, 2, 50, 60,70]
print(missingRanges(nums, 0, 99))


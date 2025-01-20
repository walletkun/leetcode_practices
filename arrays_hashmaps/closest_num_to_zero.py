'''
Leetcode 2239. Find CLosest Number to Zero
Leetcode Link: https://leetcode.com/problems/find-closest-number-to-zero/
Difficulty: Easy
Similar Problems: Find K Closest Elements
----------------------------

Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.


Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

'''


def findClosestNumber(nums):
    min_value = float('inf')

    for num in nums:
        abs_num = abs(num)
        if abs_num < abs(min_value) or (abs_num == abs(min_value) and num > min_value):
            min_value = num


    return min_value


# Debug
nums = [-2,-1,1]

print(findClosestNumber(nums))





'''
1. Initialize a variable to hold onto the minimum value that we encountered
2. We will initlaize an abs varaible to track down the absolute num to make comparison
3. But within in the comparison we must remember about the edge case of if there is a same value e.g -1, 1 we will need to return 1
4. Becuase of that we will have to remember that if the value equals to our abs value of the smallest number then we will initialize that to be our new minimum value
5. Then return that minimum value
'''
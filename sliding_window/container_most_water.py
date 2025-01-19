'''
Leetcode 11. Container With Most Water
Leetcode Link: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
Difficulty: Medium
Similar Problems: Trapping Rain Water
----------------------------

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container
'''

def maxArea(height:list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    max_height = max(height) # For optimization

    while left < right:
        distance = right - left
        min_height = min(height[right], height[left])
        max_area = max(max_area, min_height * distance)
        # For optimization
        if max_area >= max_height * (right - left):
            break

        # Move the pointers
        if height[left] < height[right]:
            left += 1

        else:
            right -= 1
            
    return max_area


# Debug
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))


'''
1. Using two pointer to dynamically locate down the max hegiht
2. Store the max area with an varaible
3. Loop through the container and checking for the minimum height every time because if a value is 8 and the other side is 7 we take the minimum
4. Track down the distance between two pointers by using right - left
5. Compare the max area with the two pointers
6. If the height of 1 pointer is less the another increment left or decrement right
7. Return the max area

# Optimization:
Store the max height in the container, and mutiplying with right - left with the max height will generate the largest area with the given distance, therefore if our max area is greater than or equal to we can just break out of it which will give us a huge optimization to early call back.
'''
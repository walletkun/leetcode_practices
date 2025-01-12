def solution(nums, target):
    # Sort the array to utilize two pointers
    # But for this question we need 3 pointers because we need 3 elements

    nums.sort()
    res = []
    n = len(nums)
    # Closest variable to keep track our closest_product
    closest_product = float('inf')
    for i in range(n - 2):

        left , right = i + 1, n - 1

        while left < right:
            cur_product = nums[i] * nums[left] * nums[right]

            if cur_product > 0 and abs(target - cur_product) < abs(target - closest_product):
                closest_product = cur_product
                res = [nums[i], nums[left], nums[right]]

            if cur_product < target:
                left += 1

            else:
                right -= 1


    return res
            

nums = [-1, 2, 3, -4]
target = 24

print(solution(nums, target))



'''
1. Sort the array
2. We have to utilize 3 pointer technique which i will be iterating from the first element, left will be 1 after and right will be from the back
to prevent missing values from the greatest
3. have a variable to keep track of our closest, and the formula where if our target - cur_sum < target - closest_num , then we can set our closest to our cur_sum
4. we just need to place it in our res list
5. return it
'''
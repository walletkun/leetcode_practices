def longest_consecutive(nums):
    max_length = 0
    elements = set(nums)

    for element in elements:
        if element + 1 not in elements: # Used to check if the starting point exist in the set
            cur_element = element
            length = 1

            while(cur_element - 1) in elements:
                cur_element -= 1
                length += 1

            max_length = max(max_length, length)
                


    return max_length

nums = [10, 1,3,4,2,20]
print(longest_consecutive(nums))
            
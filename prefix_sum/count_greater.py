'''
Problem: Count element greater than X in Ranges
Difficulty: Medium
----------------------------

Given an array of integers nums, a threshold X, and a 2D array of queries, count how many numbers are greater than X in each range [li, ri].

### Example 1:
Input:
nums = [2, 5, 8, 3, 7]
X = 4
queries = [[0, 2], [1, 4], [0, 4]]

Output: [2, 3, 3]
'''

def count_greater(nums, X, queries):
    # helper function to define if it's greater than x
    def greater_than(nums):
        return nums > X

    validate = [greater_than(num) for num in nums]
    print(validate)

    n = len(nums)
    prefix = [0] * n
    prefix[0] = 1 if validate[0] else 0

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + (1 if validate[i] else 0)

    res = []
    for li, ri in queries:
        if li == 0:
            res.append(prefix[ri])
        else:
            res.append(prefix[ri] - prefix[li - 1])

    return res


def main():
    nums = [2, 5, 8, 3, 7]
    X = 4
    queries = [[0, 2], [1, 4], [0, 4]]

    print(count_greater(nums, X, queries))


if __name__ == '__main__':
    main()
    
    

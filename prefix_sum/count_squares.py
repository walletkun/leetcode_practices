'''
Problem: Count Square number in Ranges
Difficulty: Medium
----------------------------

Given an array of integers nums and a 2D array of queries, return the sum of squares of numbers in each range [li, ri].

### Example 1:
Input:
nums = [1, 2, 3, 4]
queries = [[0, 2], [1, 3], [0, 3]]

Output: [14, 29, 30]
'''

def sum_squares(nums, queries):
    def squares(num):
        return num ** 2

    n = len(nums)
    prefix = [0] * n
    prefix[0] = squares(nums[0])

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + squares(nums[i]) # [1, 5, 14, 30]
        
    res = []
    for li, ri in queries:
        if li == 0:
            res.append(prefix[ri])
        else:
            res.append(prefix[ri] - prefix[li - 1])

    return res 
    
def main():
    nums = [1, 2, 3, 4]
    queries = [[0, 2], [1, 3], [0, 3]]

    output = sum_squares(nums, queries)
    print(output)

if __name__ == '__main__':
    main()


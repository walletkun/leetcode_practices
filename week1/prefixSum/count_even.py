'''
Problem: Count Even Numbers in Ranges
Difficulty: Medium
----------------------------

Given an array of integers `nums` and queries, count the number of even numbers in the queries that fall within the given range.  
You are given a 0-indexed array of integers `nums` and a 2D array of integers `queries`.  
Each query `queries[i] = [li, ri]` asks us to find the number of even numbers present in the range `li` to `ri` (both inclusive).  
Return an array `ans` of size `queries.length`, where `ans[i]` is the answer to the \(i\)-th query.

### Example 1:
Input:
nums = [2,4,5,6,8]
queries = [[0,3], [1,4], [2,2]]

'''

def count_even_numbers_in_ranges(nums,queries):
    # Helper function to check if a number is even
    def is_even(num):
        return num % 2 == 0

    # Precompute the prefix sum
    n = len(nums)
    prefix = [0] * n
    prefix[0] = 1 if is_even(nums[0]) else 0

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + (1 if is_even(nums[i]) else 0)

    res = []
    for li, ri in queries:
        if li == 0:
            res.append(prefix[ri])
        else:
            res.append(prefix[ri] - prefix[li - 1])

    return res


def main():
    nums = [2,4,5,6,8]
    queries = [[0,3], [1,4], [2,2]]

    output = count_even_numbers_in_ranges(nums, queries)
    print(output)


if __name__ == '__main__':
    main()
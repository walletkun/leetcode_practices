'''
Problem: Count Odd Numbers in Ranges
Difficulty: Medium
----------------------------

Given an array of integers `nums` and queries, count the number of even numbers in the queries that fall within the given range.  
You are given a 0-indexed array of integers `nums` and a 2D array of integers `queries`.  
Each query `queries[i] = [li, ri]` asks us to find the number of even numbers present in the range `li` to `ri` (both inclusive).  
Return an array `ans` of size `queries.length`, where `ans[i]` is the answer to the \(i\)-th query.

### Example 1:
Input:
nums = [1, 3, 5, 2, 4]
queries = [[0, 2], [1, 4], [0, 4]]

Output: [3, 2, 3]
'''

def odd_count(nums, queries):
    def is_odd(num):
        return num % 2 != 0

    # We first will have to initialize our validations
    validate = [is_odd(num) for num in nums]
    print(validate)

    # Build the prefixes
    n = len(validate)
    prefix = [0] * n
    prefix[0] = 1 if validate[0] else 0
    print(prefix)

    for i in range(1,n):
        prefix[i] = prefix[i - 1] + (1 if validate[i] else 0)
    
    # Build the result array
    res = []
    for li, ri in queries:
        if li == 0:
            res.append(prefix[ri])
        else:
            res.append(prefix[ri] - prefix[li - 1])

    return res
    



def main():
    nums = [1, 3, 5, 2, 4]

    queries = [[0, 2], [1, 4], [0, 4]]

    print(odd_count(nums, queries))


if __name__ == '__main__':
    main()


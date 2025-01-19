'''
Leetcode 56. Merge Intervals
Leetcode Link: https://leetcode.com/problems/merge-intervals/description/
Difficulty: Medium
Similar Problems:  Insert Interval, Meeting Rooms, Meeting Rooms 2
----------------------------
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Sort the intervals
    intervals.sort(key=lambda x : x[0])

    # Store the result array but also keep the first interval as our starting point
    res = [intervals[0]]

    for interval in intervals:

        # Keep the last interval in check
        last = res[-1]

        # There is a overlap
        if interval[0] <= last[1]:
            last[1] = max(last[1], interval[1])

        # If there is not just append the interval
        else:
            res.append(interval)


    return res



# Debug
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
        
        

    



    


'''
1. Sort the intervals first by their first values, (e.g., [5,6],[1,5] => [1,5],[5,6])
2. Initialize a start pointer, and we will iterate through the start pointer, until we meet the next interval's end pointer and we compare if our starting point exceeds that, that end pointer will be our merged intervals end pointer
3. Return the merged list
'''
        
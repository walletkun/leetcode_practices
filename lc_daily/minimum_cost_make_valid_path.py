"""
Leetcode 1368. Minimum Cost to Make at Least One Valid Path in a Grid
Leetcode Link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=daily-question&envId=2025-01-18
Difficulty: Hard
Similar Problems:  Minimum Weighted Subgraph With the Required Paths, Disconnect Path in a Binary Matrix by at Most One Flip
----------------------------

Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.
"""
from collections import deque

def solution(grid: list[list[int]]) -> int:

    # Initialize directions in a 2d array
    directions = [(0,1), (0, -1), (1,0), (-1, 0)] # Right, left, up and down
    rows, cols = len(grid), len(grid[0])
    dq = deque([(0,0,0)]) # rows, cols, and cost
    visited = set() # Initialize a set to remember if we've visted the rows, cols

    while dq:
        x,y,cost = dq.popleft() # We will pop every first value we inputted

        # If we've reached the bottom right corner
        if (x,y) == (rows - 1, cols - 1):
            return cost

        if (x,y) in visited:
            continue
        
        visited.add((x,y))

        # Check all four possible directions
        for idx, (dx, dy) in enumerate(directions, start = 1):
            nx, ny = x + dx, y + dy # new x and new y is the direction we initialized + the current cell we're in
            # Ensuring that the new direction is within the bounds
            if 0 <= nx < rows and 0 <= ny < cols:
                # If the direction matches the grid, we don't need to increment the cost
                if grid[x][y] == idx:
                    dq.appendleft((nx,ny,cost))
                else:
                    dq.append((nx,ny,cost + 1))


    return -1

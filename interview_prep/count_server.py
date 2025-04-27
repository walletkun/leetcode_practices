"""
Prompt:
You're given a grid of 0s and 1s representing servers. Return a list of coordinates for all servers that can communicate with at least one other server.

This is a direct variation of what you’ve already done, but now you return the positions instead of the count.

Example Input:

python
Copy
Edit
grid = [
    [1, 0],
    [1, 1]
]
Expected Output:

python
Copy
Edit
[(0,0), (1,0), (1,1)]
"""

def countServers(grid):
    m, n = len(grid), len(grid[0])
    row_count = [0] * m
    col_count = [0] * n
    res = []

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                row_count[r] += 1
                col_count[c] += 1


    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                res.append((r,c))


    return res


grid = [
    [1, 0],
    [1, 1]
]

print(countServers(grid))


from collections import deque
def countServers2(grid):
    # Using the brute for logic
    M, N = len(grid), len(grid[0])
    res = 0
    visited = [[False] * N for _ in range(M)]

    def bfs(i ,j):
        queue = deque()
        queue.append((i ,j))
        visited[i][j] = True
        # Group list
        group = [(i , j)]

        while queue:
            r, c = queue.popleft()

            # Checking every column in the row
            for col in range(N):
                if grid[r][col] == 1 and not visited[r][col]:
                    visited[r][col] = True
                    queue.append((r, col))
                    group.append((r, col))

            # Checking every row
            for row in range(M):
                if grid[row][c] == 1 and not visited[row][c]:
                    visited[row][c] = True
                    queue.append((row, c))
                    group.append((row, c))


        return len(group) if len(group) > 1 else 0


    # Iterate through each cell with the bfs we wrote
    for r in range(M):
        for c in range(N):
            if grid[r][c] == 1 and not visited[r][c]:
                res += bfs(r, c)


    return res


grid = [
    [1, 0],
    [1, 1]
]

print(countServers2(grid))



def countServers3(grid):
    M, N = len(grid), len(grid[0])
    visited = [[False] * N for _ in range(M)]
    group = 0

    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True

        while queue:
            r, c = queue.popleft()
            # Check all rows in current column
            for row in range(M):
                if grid[row][c] == 1 and not visited[row][c]:
                    visited[row][c] = True
                    queue.append((row, c))

            # Check all cols in current row
            for col in range(N):
                if grid[r][col] == 1 and not visited[r][col]:
                    visited[r][col] = True
                    queue.append((r, col))

    for r in range(M):
        for c in range(N):
            if grid[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                group += 1

    return group

# Test
grid = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]
print(countServers3(grid))

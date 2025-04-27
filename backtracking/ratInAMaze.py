def sol(matrix):
    n = len(matrix)
    res = []
    path = []
    def backtrack(matrix, row, col):
        # base cases to prevent invalid search
        if row < 0 or row >= n or col < 0 or col >= n or matrix[row][col] == 1: 
            return
        
        # directions we're going to visit, (up, down, right, left)
        directions = [(-1, 0, "U"),(1, 0, "D"), (0, 1, "R"), (0, -1, "L")]
        
        # Crucial ending case to the backtracking where we are at the destination now
        if row == n - 1 and col == n - 1:
            res.append("".join(path))
        else:
            # marking the cell that we're visiting as visited
            matrix[row][col] = 1

            for dr, dc, move in directions:
                nr, nc = row + dr, col + dc
                path.append(move)
                backtrack(matrix, nr, nc)
                path.pop()

            #Saving the position we're at by unmarking it
            matrix[row][col] = 0
        
    backtrack(matrix, 0, 0)
    return res
            

matrix = [[0, 1, 1, 1], 
          [0, 0, 1, 0], 
          [1, 0, 1, 1], 
          [0, 0, 0, 0]]
print(sol(matrix))
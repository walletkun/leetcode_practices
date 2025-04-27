def create_board(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    return board

def sol(n):
    def backtrack(matrix, r, c, move_count):
        if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] != -1:
            return False

        # mark the current cell
        matrix[r][c] = move_count
        
        if move_count == n * n - 1:
            return True

        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if backtrack(matrix, nr, nc, move_count + 1):
                return True
        # backtrack
        matrix[r][c] = -1
        return False


    board = create_board(n)
    backtrack(board, 0, 0, 0)
    return board


solution = sol(5)
for row in solution:
    print(row)
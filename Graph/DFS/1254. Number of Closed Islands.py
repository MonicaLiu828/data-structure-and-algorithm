class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        visited = set()
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if (i, j) in visited:
                return True
            if grid[i][j] == 1:
                visited.add((i, j))
                return True
            if (i, j) not in visited:
                visited.add((i, j))

            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            if left and right and up and down:
                return True

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1
        return count




class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def dfs(r, c):
            max1 = 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r, c) in seen:
                return max1
            if (r, c) not in seen:
                seen.add((r, c))
                max1 += 1
                max1 += dfs(r + 1, c)
                max1 += dfs(r - 1, c)
                max1 += dfs(r, c + 1)
                max1 += dfs(r, c - 1)
                return max1

        preMax = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    preMax = max(dfs(row, col), preMax)
        return preMax

        # time:O(M*N)
        # space:O(M*N)
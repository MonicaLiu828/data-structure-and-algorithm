class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # i = row, j = column
        def dfs(i,j):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j]== '0':
                return
            if grid[i][j] == '2':
                return
            if grid[i][j] == '1':
                grid[i][j] = '2'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count
    # time: o(m*n)
    # space: o(m*n)
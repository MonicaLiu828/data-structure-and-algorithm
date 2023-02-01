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

    solution 2:

    class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
            seen = set()
            count = 0

            def dfs(i, j):
                direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) \
                        in seen or grid[i][j] == '0':
                    return
                if (i, j) not in seen:
                    seen.add((i, j))
                for row, col in direction:
                    dfs(i + row, j + col)

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1' and (i, j) not in seen:
                        # seen.add(grid[i][j])
                        count += 1
                        dfs(i, j)

            return count
        # time: o(m*n)
        # space: o(m*n)
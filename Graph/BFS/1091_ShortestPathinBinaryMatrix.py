class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        seen = set()
        seen.add((0,0))
        direction = [(0,1),(1,1),(-1,0),(-1,-1),(1,0),(0,-1),(-1,1),(1,-1)]
        stor = deque()
        stor.append((0,0,1))
        r = l = 0
        s = 1
        while stor:
            currItem = stor.popleft()
            r = currItem[0]
            l = currItem[1]
            s = currItem[2]
            if r == l == len(grid)-1:
                return s
            for item in direction:
                row = r+item[0]
                col = l+item[1]
                if (row,col) not in seen and row >= 0 and col >= 0 and row < len(grid) and col < len(grid)\
                and grid[row][col] != 1:
                    seen.add((row,col))
                    stor.append((row,col,s+1))
        return -1

Time complexity : O(N)O(N)O(N).

Same as approach 1. Processing a cell is O(1)O(1)O(1), and each of the NNN cells is processed at most once, giving a total of O(N)O(N)O(N).

Space complexity : O(N)O(N)O(N).

Same as approach 1. The visited set also requires O(N)O(N)O(N) space; in the worst case, it will hold the row and column of each of the NNN cells.
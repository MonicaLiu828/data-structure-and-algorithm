class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(grid)
        cols = len(grid[0])
        fresh = set()
        rotten = deque()
        emp = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                if grid[row][col] == 2:
                    rotten.append((row, col))
        # print(fresh,rotten)
        count = 0
        while fresh and rotten:

            # if len(fresh) == 0:
            #     return count

            for _ in range(len(rotten)):
                item = rotten.popleft()
                print(item)
                for direction in directions:
                    newrow = item[0] + direction[0]
                    newcol = item[1] + direction[1]

                    if newrow < rows and newcol < cols and newrow > -1 \
                            and newcol > -1 and (newrow, newcol) in fresh:
                        fresh.remove((newrow, newcol))
                        rotten.append((newrow, newcol))

            count += 1
        # print(fresh, rotten)
        if fresh:
            return -1
        return count

        # visit, curr = set(), deque()
    # # find all fresh and rotten oranges
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             visit.add((i, j))
    #         elif grid[i][j] == 2:
    #             curr.append((i, j))
    # result = 0
    # while visit and curr:
    # 	# BFS iteration
    #     for _ in range(len(curr)):
    #         i, j = curr.popleft()  # obtain recent rotten orange
    #         for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
    #             if coord in visit:  # check if adjacent orange is fresh
    #                 visit.remove(coord)
    #                 curr.append(coord)
    #     result += 1
    # # check if fresh oranges remain and return accordingly
    # return -1 if visit else result

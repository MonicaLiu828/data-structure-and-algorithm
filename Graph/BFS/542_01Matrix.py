class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # iterate this matrix
        # if it's 0 return 0
        #  if it's 1 from this point to go through each direction(not go over boundary)
        # find its shortest distance from 0 (BFS)

        # another solution to find all 0 at first then find its reletive 1:
        direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        r = len(mat)
        c = len(mat[0])
        seen = set()
        stor = deque()

        for row in range(r):
            for col in range(c):
                if mat[row][col] == 0:
                    seen.add((row, col))
                    stor.append([row, col, 1])
        while stor:
            r1, c1, s1 = stor.popleft()
            for item in direction:
                r2 = r1 + item[0]
                c2 = c1 + item[1]
                if (r2, c2) not in seen and r2 >= 0 and r2 < r and c2 < c and c2 >= 0:
                    seen.add((r2, c2))
                    mat[r2][c2] = s1
                    stor.append([r2, c2, s1 + 1])

        return mat

        # time: O(N*M)
        # space: O(N*M)

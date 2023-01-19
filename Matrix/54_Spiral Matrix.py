class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # row
        m = len(matrix)
        # column
        n = len(matrix[0])
        # 4 boundaries
        left = top = 0
        right = n - 1
        bottom = m - 1

        res = []
        while len(res) < m * n:

            # left->right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            # top->bottom
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])

            # right->left:
            # to handle only one row, to make it not run left to right then go back to left again
            if bottom != top:
                for h in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][h])

            # bottom -> top:
            #  to handle only one column, to make it not run bottom to top after it has loop from top to bottom
            if left != right:
                for k in range(bottom - 1, top, -1):
                    res.append(matrix[k][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res

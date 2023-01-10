class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # each row's first number to make sure which row to check
        # binary search of target row
        # up_row = 0
        # dow_row = len(matrix)-1
        # while up_row <= dow_row:
        #     m_rownum = (matrix[up_row][0]+matrix[dow_row][0])//2
        #     if m_rownum == target:
        #         return True
        #     elif up_row == dow_row:
        #         return up_row
        #     elif matrix[m_row][0] < target:
        #         up_row = m_row
        #     elif matrix[m_row][0]> target:
        #         dow_row = m_row - 1
        # l = 0
        # r = len(matrix[up_row])-1
        # while l <= r:
        #     m =(matrix[up_row][l]+matrix[up_row][r])//2
        #     if matrix[up_row][m] == target:
        #         return True
        #     elif matrix[up_row][m] < target:
        #         l = matrix[up_row][m]+1
        #     else:
        #         r = matrix[up_row][m]-1
        # return False
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            middle = (l + r) // 2
            row = middle // n
            col = middle % n
            num = matrix[row][col]
            if num == target:
                return True
            elif num > target:
                r = middle - 1
            else:
                l = middle + 1
        return False

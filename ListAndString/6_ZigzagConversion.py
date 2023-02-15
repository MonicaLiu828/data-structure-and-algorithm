class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        idx = 0
        step1 = 1
        if numRows == 1:
            return s
        for item in s:
            rows[idx] += item
            if idx == numRows - 1 or (idx == 0 and step1 == -1):
                step1 = -1 * step1
            idx += step1

        return ''.join(rows)

# Time complexity: O(n)->n is length of s
# Space complexity: O(1)-> space = numRows
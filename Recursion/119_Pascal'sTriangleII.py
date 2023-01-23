class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        # if rowIndex == 1:
        #     return[1,1]
        res = []
        res.append (1)
        if rowIndex-1 >= 0:
            prevRow = self.getRow(rowIndex-1)
            for i in range(len(prevRow)-1):
                sum = prevRow[i]+ prevRow[i+1]
                res.append(sum)
        res.append(1)
        return res

    # time:  O(k*K)->o(k2)
    # space: O(k)
    # For the k, k is the Kth row
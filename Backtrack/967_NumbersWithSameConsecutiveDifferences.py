class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def backtrack(str1):
            if len(str1) == n:
                res.append(int(str1))
                return
            for j in range(0,10):
                if abs(j-int(str1[-1])) == k:
                    backtrack(str1+str(j))
        for i in range (1,10):
            string = str(i)
            backtrack(string)
        return res

        # time: n*2power(n-1)
        # space: n*2power(n-1)
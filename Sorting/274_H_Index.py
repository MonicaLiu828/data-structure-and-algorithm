class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        res = 0
        print(citations)
        for i, item in enumerate(citations):
            if citations[i] >= i + 1:
                res += 1
            else:
                break
        return res










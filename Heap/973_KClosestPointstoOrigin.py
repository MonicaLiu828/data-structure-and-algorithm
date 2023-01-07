class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for item in points:
            sum = item[0] * item[0] + item[1] * item[1]
            heapq.heappush(minheap, [sum, item])
        res = []
        count = 0
        while count < k:
            popped = heapq.heappop(minheap)
            res.append(popped[1])
            count += 1
        return res

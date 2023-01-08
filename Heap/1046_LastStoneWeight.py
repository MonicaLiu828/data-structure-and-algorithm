class Solution:
    # maxheap
    # pop 2 times
    # push difference
    # repeat
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-item for item in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            first = abs(heapq.heappop(maxheap))
            second = abs(heapq.heappop(maxheap))
            if first != second:
                heapq.heappush(maxheap, second - first)

        if len(maxheap) == 1:
            return abs(maxheap[0])
        else:
            return 0
# time: O(n) + O(n) + n * 2(O(logn)) -> nlog(n)
# space: O(2n) -> O(n)
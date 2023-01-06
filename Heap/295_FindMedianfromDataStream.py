class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)
        heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        average = 0
        if len(self.maxheap) == len(self.minheap):
            average = (self.minheap[0]-self.maxheap[0])/2
        if len(self.maxheap) > len(self.minheap):
            average = -self.maxheap[0]
        return average


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
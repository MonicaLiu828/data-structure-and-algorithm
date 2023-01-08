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

# Time:
# add: 5log(n/2) -> logn (n is the length of data stream)
# find: O1

# Space:
# O(n)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# entire stream in asc sorted order:
# numbers on the left side: maxHeap
# numbers on the right side: minHeap
# maxHeap top is below minheap top, each time -> each element goes into maxheap, then popped max to minheap, then
# put top of minheap to max if minheap length > maxheap length, it will make sure maxheap over minheap one number or
# maxheap length == minheap length

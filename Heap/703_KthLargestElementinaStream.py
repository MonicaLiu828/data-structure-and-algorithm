class KthLargest:
    # minheap
    # pop to left k's number of element
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
            return self.minheap[0]
        elif val <= self.minheap[0]:
            return self.minheap[0]
        else:
            heapq.heappush(self.minheap, val)
            heapq.heappop(self.minheap)
            return self.minheap[0]

# time:
# init: O(n) + (n-k)logn  (n is the length of nums )
# add: 2*logk- > logk  (k is k's number of elements)

# space: O(N)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
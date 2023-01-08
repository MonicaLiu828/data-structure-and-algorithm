class Solution:
    def halveArray(self, nums: List[int]) -> int:
        count = 0
        sum = 0
        minheap = []
        for item in nums:
             minheap.append(-item)
             sum = sum + item
        heapq.heapify(minheap)
        average = sum/2
        while average > 0:
            popped = heapq.heappop(minheap)/2
            average = average + popped
            count += 1
            heapq.heappush(minheap,popped)
        return count

# time: O(nlogn)
# space: O(n)
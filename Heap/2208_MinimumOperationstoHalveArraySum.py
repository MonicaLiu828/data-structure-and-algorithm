class Solution:
    def halveArray(self, nums: List[int]) -> int:
        count = 0
        minheap = [-item for item in nums]
        heapq.heapify(minheap)
        average = sum(nums)/2
        while average > 0:
            popped = heapq.heappop(minheap)/2
            average = average + popped
            count += 1
            heapq.heappush(minheap,popped)
        return count

# time: O(nlogn)
# space: O(n)
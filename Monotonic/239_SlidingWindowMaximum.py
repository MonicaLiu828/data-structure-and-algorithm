class Solution:
    # queue to store all elements
    # index to find max, compare new one to max
    def __init__(self):
        self.queue = deque()
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res_arr = []
        for index, num in enumerate(nums):
            while self.queue and num > nums[self.queue[-1]]:
                self.queue.pop()
            self.queue.append(index)
            if index - self.queue[0] == k:
                self.queue.popleft()
            if index >= k -1:
                res_arr.append(nums[self.queue[0]])
        return res_arr




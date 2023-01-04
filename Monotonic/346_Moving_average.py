class MovingAverage:
# store all integers
# enqueue and then check size
# if > size, dequeue

    def __init__(self, size: int):
        self.queue = deque()
        self.size =size
        self.sum = 0
    def next(self, val: int) -> float:
        # if self.size > 0:
        self.queue.append(val)
        if len(self.queue) > self.size:
            first_item = self.queue.popleft()
            self.sum = self.sum - first_item
        self.sum = self.sum + val
        return self.sum/len(self.queue)

# step1: define a new deque and give a global sum to store all deuque's sum
# step2: append new value and check if size > original size, pop deque and make the sum - poped item
# step3: get new sum and get the average result
# tips:  self.queue = deque([],size)will pop automatically if after appending the lenght > size

# time: O(1)
# space:O(n)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
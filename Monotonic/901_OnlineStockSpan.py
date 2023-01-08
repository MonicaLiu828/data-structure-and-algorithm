class StockSpanner:
    def __init__(self):
        self.stack = []
        self.dict = {}

    #  use map to store each number's answer
    # stack to store decrease number, since it requires consecutive days
    #  if new num > stack top, pop and push
    def next(self, price: int) -> int:
        answer = 0
        if not self.stack:
            self.stack.append(price)
            answer = 1
            self.dict[price] = answer
        else:
            while self.stack and price >= self.stack[-1]:
                popped = self.stack.pop()
                answer = answer + self.dict[popped]
            self.stack.append(price)
            answer = answer + 1
            self.dict[price] = answer
        return answer

# time: O(1) -> each number will be popped at most once, in amortized analyze, each time should be O(1)
# space: O(2n) -> O(n)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
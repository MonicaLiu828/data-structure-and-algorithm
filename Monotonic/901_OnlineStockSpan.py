class StockSpanner:
    def __init__(self):
        self.stack = []
        self.dict = {}

    def next(self, price: int) -> int:
        answer = 0
        if not self.stack:
            self.stack.append(price)
            answer = 1
            self.dict[price] = answer
            return answer
        else:
            while self.stack and price >= self.stack[-1]:
                popped = self.stack.pop()
                answer = answer + self.dict[popped]
            self.stack.append(price)
            answer = answer + 1
            self.dict[price] = answer
        return answer

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
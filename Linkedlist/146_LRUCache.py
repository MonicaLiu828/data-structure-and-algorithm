class DoubleListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def addListAnddict(self, key, val):
        # always add to head's next
        newNode = DoubleListNode(key, val)
        next_node = self.head.next
        self.head.next = newNode
        newNode.next = next_node
        newNode.prev = self.head
        next_node.prev = newNode

    def popFromTail(self):
        poppedNode = self.tail.prev
        prev_node = self.tail.prev.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        del self.dict[poppedNode.key]

    def moveCurrNextToHead(self, key):
        # Node = DoubleListNode(key,self.dict[key])
        pointer = self.head
        while pointer:
            if pointer.key == key:
                Node = pointer
                Node.next.prev = Node.prev
                Node.prev.next = Node.next

                next_node = self.head.next
                self.head.next = Node
                Node.next = next_node
                Node.prev = self.head
                next_node.prev = Node
                break
            pointer = pointer.next

    def __init__(self, capacity: int):
        self.currCount = 0
        self.dict = {}
        self.size = capacity
        self.head = DoubleListNode(-1, -1)
        self.tail = DoubleListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            value = self.dict[key]
            self.moveCurrNextToHead(key)
            return value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.moveCurrNextToHead(key)
        else:
            if self.currCount + 1 <= self.size:
                self.dict[key] = value
                self.addListAnddict(key, value)
                self.currCount += 1
            elif self.currCount + 1 > self.size:
                self.dict[key] = value
                self.addListAnddict(key, value)
                self.popFromTail()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
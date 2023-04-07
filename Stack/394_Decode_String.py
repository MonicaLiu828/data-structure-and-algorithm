class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        stor = deque()
        res = ''
        for item in s:
            if item != ']':
                stack.append(item)
            if item == ']':
                while not stack[-1].isdigit():
                    popped_item = stack.pop()
                    if popped_item == '[':
                        continue
                    stor.append(popped_item)
                count = deque()

                while stack and stack[-1].isdigit():
                    count.append(stack.pop())
                freq_str = ''
                while count:
                    freq_str += count.pop()
                freq = int(freq_str)
                stor = int(freq) * stor

                if len(stack) > 0:
                    while stor:
                        popped_item = stor.pop()
                        stack.append(popped_item)
                else:
                    while stor:
                        popped_item = stor.pop()
                        res += popped_item
        if stack:
            while stack:
                item = stack.popleft()
                res += item
        return res








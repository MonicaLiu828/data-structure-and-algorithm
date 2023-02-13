class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stor = defaultdict(list)
        for i in range(len(arr)):
            newVal = i + arr[i]
            newVal2 = i - arr[i]
            if newVal >= 0 and newVal <len(arr):
                stor[i].append(newVal)
            if newVal2 >= 0 and newVal2 <len(arr):
                stor[i].append(newVal2)
        #  0:[4] 1:[3]
        seen = set()
        queue = deque()
        seen.add(start)
        queue.append([start,arr[start]])
        while queue:
            idx,val = queue.popleft()
            if val == 0:
                return True
            for idx2 in stor[idx]:
                if idx2 not in seen:
                    seen.add(idx2)
                    queue.append([idx2,arr[idx2]])
        return False
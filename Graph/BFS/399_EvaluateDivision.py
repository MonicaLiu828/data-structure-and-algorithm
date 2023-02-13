class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        stor = defaultdict(list)
        for i in range(len(equations)):
            storKey = equations[i][0]
            storVal = equations[i][1]
            stor[storKey].append((storVal, values[i]))
            newReverseVal = 1 / values[i]
            stor[storVal].append((storKey, newReverseVal))
        #  a: [[b:2]]
        #  b: [[a,0.5],[c:3]]
        #  c: [[b:1/3]]
        res = []

        def bfs(start, value, target):
            seen = set()
            seen.add(start)
            queue = deque()

            if start in stor:
                # handle a/a
                if target == start:
                    res.append(1.0)
                    return
                for setVal in stor[start]:
                    # find start point add all elements of this key in map to queue
                    queue.append(setVal)
                while queue:
                    key, val = queue.popleft()
                    if key not in seen and key != target:
                        seen.add(key)
                        #  loop b as key each element:
                        for item in stor[key]:
                            # exclude [a:0.5] into queue again
                            if item[0] not in seen:
                                #  add [c:2*3] into queue
                                queue.append([item[0], val * item[1]])
                    if key not in seen and key == target:
                        res.append(val)
                        return
                #  to handle if we want to check a/e, e is not in this map so queue will finally become [], we need to add
                #  add -1 into res instead of doing nothing
                res.append(-1.0)
                return
            else:
                # handle[e/e]
                res.append(-1.0)
                return

        for item in queries:
            bfs(item[0], 1, item[1])
        return res
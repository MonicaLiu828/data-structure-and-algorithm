class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        redMap = defaultdict(list)
        blueMap = defaultdict(list)
        for item in redEdges:
            redMap[item[0]].append(item[1])
        for item in blueEdges:
            blueMap[item[0]].append(item[1])

        red = 0
        blue = 1
        res = [float('inf')] * n

        seen = set()
        seen.add((0, red))
        seen.add((0, blue))
        stor = deque()
        stor.append((0, red, 0))
        stor.append((0, blue, 0))
        while stor:
            node, col, step = stor.popleft()
            if res[node] == float('inf'):
                res[node] = step
            if col == 0:
                for item in redMap[node]:
                    if (item, red) not in seen:
                        seen.add((item, red))
                        stor.append((item, blue, step + 1))
            if col == 1:
                for item in blueMap[node]:
                    if (item, blue) not in seen:
                        seen.add((item, blue))
                        stor.append((item, red, step + 1))

        for i in range(0, len(res)):
            if res[i] == float("inf"):
                res[i] = -1
        return res

# time: O(n+e)
# space:O(n+e) N is the total number of node, e is the total number of edge



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        stor = defaultdict(list)
        seen = set()
        for arr in edges:
            stor[arr[0]].append(arr[1])
            stor[arr[1]].append(arr[0])
        self.res = False
        def dfs(start):
            if start == destination:
                self.res = True
            if start not in seen:
                # print(True)
                seen.add(start)
                for item in stor[start]:
                    dfs(item)
        dfs(source)
        # print(res)
        return self.res

# time: O(N+E)
# space:O(N+E)
# We use a hash map to store m edges, it takes O(m)space.
# We use one bool array seen to record visited nodes, which also takes O(n)space.
# We use a stack stack to store all nodes to be visited, in the worst-case scenario,there may be O(n)nodes in stack.
# To sum up, the space complexity is O(n+m).

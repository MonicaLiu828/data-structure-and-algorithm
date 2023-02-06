class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        stor = defaultdict(list)
        # store each seen node
        seen = set()
        #stor original edge with directions
        road = set()
        for x,y in connections:
            stor[x].append(y)
            stor[y].append(x)
            road.add((x,y))
        # self.ans = 0
        # find a minimum reversed edge from node to its neighor or neibor's neibor's neighbor
        # those neighbor have not been seen
        def dfs(node):
            answer = 0
            for item in stor[node]:
                if item not in seen:
                    seen.add(item)
                    if (node,item) in road:
                        answer+=1
                    answer = answer + dfs(item)
            return answer
        seen.add(0)
        return dfs(0)
        # time and space both are O(N) since edge is length of connections -1


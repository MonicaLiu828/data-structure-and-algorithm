class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # convert list of node into hash map, key is node value is the arr
        # of its connected node, this will get a dict with each node and its releted
        #  connected nodes
        stor = defaultdict(list)
        num = len(isConnected)
        for i in range(num):
            for j in range(i + 1, num):
                if isConnected[i][j] == 1:
                    stor[i].append(j)
                    stor[j].append(i)

        # set up a set to avoid infinity loop of undirected edge and final answer
        seen = set()
        ans = 0

        # dfs from one node to traverse all other node connected with this original node
        # and mark all of them as seen, but the whole answer should be one, since they are
        #  all connected city like example 1: 1-2
        def dfs(node):
            for item in stor[node]:
                if item not in seen:
                    seen.add(item)
                    dfs(item)

        #  loop each node key in dict, if it has not been visited add one to ans and
        #  dfs it and mark it as seen
        for k in range(num):
            if k not in seen:
                ans += 1
                seen.add(k)
                dfs(k)
        return ans

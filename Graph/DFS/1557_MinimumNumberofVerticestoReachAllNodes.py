class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 0:[0,1,2]
        # 1:[1]
        # 2:[2,5]
        # 3:[3,4]
        # 4:[4,2]
        # 5:[5]
        res = []
        stor = defaultdict(list)
        freq = dict()
        check = set()
        for i in range(n):
            check.add(i)
            stor[i].append(i)
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for item in edges:
            stor[item[0]].append(item[1])
            if item[1] not in freq:
                freq[item[1]] = 1
            else:
                freq[item[1]] += 1
        for key in freq:
            if freq[key] == 1:
                res.append(key)
        return res

        # time O(N)
        # space:O(N)

        # dfs:
        maxstart = [0, len(stor[0])]
        for key in stor:
            if len(stor[key]) > maxstart[1]:
                maxstart = [key, len(stor[key])]

        #  dfs(0)
        if freq[maxstart[0]] == 1:
            res.append(maxstart[0])

        def dfs(start1):
            check.remove(stor[start1][0])
            for i in range(1, len(stor[start1])):
                if stor[start1][i] in check:
                    dfs(stor[start1][i])

        dfs(maxstart[0])
        checkcopy = check.copy()
        # choose next start point

        for item in checkcopy:
            count = freq[item]
            if count == 1:
                res.append(item)
                check.remove(item)
            for j in range(1, len(stor[item])):
                if stor[item][j] in check:
                    if item not in res:
                        res.append(item)
                    dfs(item)
        return res


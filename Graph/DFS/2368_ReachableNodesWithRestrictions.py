class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        stor = defaultdict(list)
        for item in edges:
            if item[0] != restricted:
                stor[item[0]].append(item[1])
                stor[item[1]].append(item[0])
        # 0:[1,4,5]
        # 1:[0,2,3]
        # 2:[1]
        # 3:[1]
        # 4:[0]
        # 5:[0,6]
        # 6:[5]
        seen = set()
        seen.add(0)
        for item in restricted:
            seen.add(item)

        def dfs(num):
            count = 0
            if num in seen:
                return count
            if num not in seen:
                seen.add(num)
                count += 1
                for item in stor[num]:
                    count += dfs(item)
                return count
        maxNum = 1
        # for key in stor:
        for eachNum in stor[0]:
            if eachNum not in restricted:
                maxNum += dfs(eachNum)
        return maxNum
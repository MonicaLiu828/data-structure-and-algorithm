class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        road = defaultdict(list)
        for item in roads:
            road[item[0]].append(item[1])
            road[item[1]].append(item[0])
        #  0:[1,2,3] 1:[0]

        # this is total minimum fuel for this roads
        self.totalSum = 0

        # this function will return total number of nodes including curr itself and all its allsprings
        #   in this function it will also record total fuels from its offspring to its releted parent and
        #  from its highest parent to its' parent's parent
        def dfs(curr, prev):
            sumNode = 1
            for node in road[curr]:
                #  make sure 1 will not go back to 0 again
                if prev == node:
                    continue
                if not node:
                    #  at this moment, node is root node's next node which is null
                    #  at this moment rootnode goes to its upper parent, cost 1 fuel
                    self.totalSum += 1
                    #  sumNode will not ++ since this moment sumNode is equal to 1 (line 16)
                    return sumNode
                sumNode += dfs(node, curr)
            #  since 0 has no parent, we don't need to calculate 0 goes to its parent's fuel cost
            if curr != 0:
                #  if at parent node, when it goes to its upper parent,
                #  it will cost ceiling of totalnode /seats and this will not handle
                #  its childern's children goes to their parent, it has been handled by line(24)
                self.totalSum += math.ceil(sumNode / seats)
            return sumNode

        dfs(0, 0)
        return self.totalSum



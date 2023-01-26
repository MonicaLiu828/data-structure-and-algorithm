class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # find which node is final node -> get the index of []
        # explore each node, if this nodelist has final node, return this path
        # else get this node's related nodelist, get nodenumber bigger than current node
        finalNode = len(graph) - 1
        res = []

        def backtrack(currArr, number):
            if currArr[-1] == finalNode:
                res.append(currArr[:])
                return
            for item in graph[number]:
                # if item != number:
                currArr.append(item)
                backtrack(currArr, item)
                currArr.pop()

        backtrack([0], 0)
        return res
# space: O(2N) -> n is the length of graph list, stack has n's recursion, and copy has n' space
# time: O(2powern*n) -> since each node can have two choice and can back
# so three nodes have 1*2*1+1*1*1's count
# 4 nodes have 1*2*2*1+1*2*1*1+1's count
# n nodes have 2power(n-1)+1 around equals to 2powern
# so should have around 2powern's count and copy has n's runtime so totoal should be 2powern*n

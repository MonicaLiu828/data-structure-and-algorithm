class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old_to_new = {}

        # copy this node and its neighbors, return clone of this node and its neibors
        def dfs(node):
            if not node:
                return None
            if not (node in old_to_new):
                if node: copy = Node(node.val)
                old_to_new[node] = copy
                if node:
                    for nei in node.neighbors:
                        copy.neighbors.append(dfs(nei))
                return copy

        return dfs(node)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        stor = defaultdict(list)
        # convert binary tree into a undirected graph:
        def dfs(node):
            if not node:
                return
            if node.left:
                stor[node.val].append(node.left.val)
                stor[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                stor[node.val].append(node.right.val)
                stor[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        # bfs graph map to find k times from target:
        seen = set()
        seen.add(target.val)
        bfs = deque()
        bfs.append((target.val, 0))
        res = []
        while bfs:
            leftItem = bfs.popleft()
            for item in stor[leftItem[0]]:
                if item not in seen:
                    seen.add(item)
                    if leftItem[1] + 1 == k:
                        res.append(item)
                    bfs.append((item, leftItem[1] + 1))

        return res

        # time: O(N)
        # space: O(N)


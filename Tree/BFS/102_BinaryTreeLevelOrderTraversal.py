class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # write your code here
        queue = deque()
        queue.append(root)
        queue.append(None)
        res =[]
        level = []
        while queue:
            node = queue.popleft()
            if node == None:
                res.append(level)
                level = []
                if queue:
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


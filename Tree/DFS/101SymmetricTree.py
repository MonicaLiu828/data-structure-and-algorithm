class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            return is_mirror(node1.left, node2.right) and \
                is_mirror(node1.right, node2.left)

        return is_mirror(root.left, root.right)
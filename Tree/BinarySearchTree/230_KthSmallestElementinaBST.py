# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stor = []
        while root:
            stor.append(root)
            root = root.left
        for i in range(k - 1):

            node = stor[-1]
            if node.right:
                node = node.right
                while node:
                    stor.append(node)
                    node = node.left
            else:
                popped_node = stor.pop()
                while stor[-1].right == popped_node and len(stor) != 0:
                    popped_node = stor.pop()
        return stor[-1].val

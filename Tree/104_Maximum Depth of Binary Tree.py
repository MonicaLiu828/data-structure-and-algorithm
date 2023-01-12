# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root and not root.left and not root.right:
            return 1
        if not root:
            return 0
        left_legth = self.maxDepth(root.left)
        right_legth = self.maxDepth(root.right)
        return max(left_legth,right_legth)+1

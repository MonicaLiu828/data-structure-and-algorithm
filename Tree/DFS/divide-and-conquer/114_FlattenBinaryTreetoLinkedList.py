# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        if not root.left and root.right:
            self.flatten(root.right)
            return
        # if root.left and root.left.left == None and root.left.right == None:
        #     if not root.right:
        #         root.right = root.left
        #         root.left = None
        #     else:
        #         original_right_node = root.right
        #         root.left.right = original_right_node
        #         root.right = root.left
        #         root.left = None

        self.flatten(root.left)
        self.flatten(root.right)
        p = root.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None


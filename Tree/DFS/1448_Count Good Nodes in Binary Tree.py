# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        def helperfunc(node, maxval):
            if not node:
                return
            if node.val >= maxval:
                maxval = node.val
                self.count += 1
            helperfunc(node.left, maxval)
            helperfunc(node.right, maxval)

        helperfunc(root, root.val)
        return self.count

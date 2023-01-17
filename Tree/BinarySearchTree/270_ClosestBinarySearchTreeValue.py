# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diff = float('inf')
        self.value = 0
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return
        if root.val == target:
            return root
        if root.val < target:
            if root.right and abs(root.right.val - target) < self.diff:
                self.diff = abs(root.right.val - target)
                self.value = root.right.val
            r = self.closestValue(root.right,target)
        else:
            if root.left and abs(root.left.val - target) < self.diff:
                self.diff = abs(root.left.val - target)
                self.value = root.left.val
            l = self.closestValue(root.left,target)
        if self.diff < abs(root.val-target):
            return self.value
        else:
            return root.val

        # time: O(n)
        # space:o(n)
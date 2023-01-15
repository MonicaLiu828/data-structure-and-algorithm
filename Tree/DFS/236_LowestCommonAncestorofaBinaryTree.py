# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root.left and root.right and root.left.val == p.val and root.right.val == q.val:
            return root
        elif root.left and root.right and root.right.val == p.val and root.left.val == q.val:
            return root
        elif root.val == p.val or root.val == q.val:
            return root
        if root.val != p.val and root.val != q.val:
            l = self.lowestCommonAncestor(root.left,p,q)
            r = self.lowestCommonAncestor(root.right,p,q)
            if l == None:
                return r
            if r == None:
                return l
        return root


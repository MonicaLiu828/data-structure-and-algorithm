# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # arr = []
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     arr.append(root.val)
        #     inorder(root.right)
        # inorder(root)

        # for i in range(len(arr)-1):
        #     if arr[i] >= arr[i+1]:
        #         return False
        # return True

        # define a function accept a root, and uuper and lower value
        # to judge if a root value is in this range, if yes, return true
        def varify(root):
            if not root:
                return True
            if lower >= root.val or root.val >= upper:
                return False
            left = varify(root.left, lower, root.val)
            #     right = varify(root.right,root.val,upper)
            if left and right:
                return True
            else:
                return False

        return varify(root, float('-inf'), float('inf'))
        if not root:
            return True
        if root.left.val >= root.val or root.right.val <= root.val:
            return False
        if root.left.val < root.val and root.right.val > root.val:
            l = varify(root.left)
            r = varfiy(root.right)
            if l and r:
                return True
            else:
                return False

    return varify(root)


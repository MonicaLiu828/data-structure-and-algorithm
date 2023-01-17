# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # arr = []
        # def helper(root):
        #     if not root:
        #         return
        #     if not root.left and not root.right:
        #         return
        #     if root.left and not root.right:
        #         left = abs(root.val-root.left.val)
        #         arr.append(left)
        #     if root.right and not root.left:
        #         right = abs(root.val-root.right.val)
        #         arr.append(right)
        #     if root and root.left and root.right:
        #         left =  abs(root.val-root.left.val)
        #         right =  abs(root.val-root.right.val)
        #         if root.left and root.right and left < right:
        #             min = left
        #             arr.append(min)
        #         else:
        #             arr.append(right)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # arr.sort()
        # return arr[0]
        arr = []
        def dfs(root):
            if not root:
                return
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        count = float("inf")
        arr.sort()
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) <count:
                count =  abs(arr[i+1]-arr[i])
        return count
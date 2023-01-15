# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # def total(root):
        #     if not root:
        #         return [0,0]
        #     leftsum = total(root.left)
        #     rightsum = total(root.right)
        #     return[leftsum[0]+root.val, rightsum[0]+root.val]
        # result = total(root)
        # if result[0] == targetSum:
        #     return True
        # if result[1] == targetSum:
        #     return True
        # else:
        #     return False

        # def total(node,curr):
        #     if not node:
        #         return False
        #     if node.left == None and node.right == None:
        #         if curr+ node.val == targetSum:
        #             return True
        #         else:
        #             return False
        #     curr = curr + node.val
        #     # total(node.left,curr)
        #     total(node.right,curr)
        #     return total(node.left,curr) or total(node.right,curr)
        # return total(root,0)

        if not root:
            return False
        if root.left == None and root.right == None:
            if targetSum - root.val == 0:
                return True
            else:
                return False
        leftPath = self.hasPathSum(root.left, targetSum - root.val)
        rightPath = self.hasPathSum(root.right, targetSum - root.val)
        return leftPath or rightPath

    # Time: O(n)
    # space: O（n) but if it's complete binanry tree should be o(logn)


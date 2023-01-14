# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # input root, output from leaf of this root, which way is the the longest, return the longest edge to this root node
        def helper(root):
            if not root:
                return -1
            if not root.left and not root.right:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            if l + r + 2 > self.result:
                self.result = l + r + 2
            return max(l, r) + 1

        helper(root)
        return self.result

        # if not root.left:
        #     return helper(root.right)+1
        # if not root.right:
        #     return helper(root.left)+1
        # maxleft = helper(root.left)
        # maxright = helper(root.right)
        # if  maxright == -1 and maxleft == -1:
        #     return 0
        # if maxleft == -1:
        #     if maxright+1 > self.result:
        #         self.result = maxright+1
        #         return self.result
        # elif maxright == -1:
        #     if maxleft+1 > self.result:
        #         self.result = maxleft+1
        #         return self.result

        # else:
        #     if maxleft+maxright+2 > self.result:
        #         self.result = maxleft+maxright+2
        #    return self.result



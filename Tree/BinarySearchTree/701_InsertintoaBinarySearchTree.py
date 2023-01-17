# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root:
        #     return TreeNode(val)
        # else:
        #     if root.val < val:
        #         root.right = self.insertIntoBST(root.right,val)
        #     else:
        #         root.left = self.insertIntoBST(root.left,val)
        # return root

        # # time:O(n)
        # # space:O(n)
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if val < node.val:
                    if not node.left:
                        node.left = TreeNode(val)
                        return root
                    else:
                        node = node.left
        # time: O(n)
        # space： O(1)

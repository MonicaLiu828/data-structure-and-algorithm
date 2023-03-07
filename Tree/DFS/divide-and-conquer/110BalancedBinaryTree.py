# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         #    helperfunc to give a node, return whether it's balanced and its height
#         def is_balance_and_high(node):
#             if not node:
#                 return True, 0
#             #  judge its left and right tree, get its balanced or not and its height
#             leftValue, leftHighet = is_balance_and_high(node.left)
#             rightValue, rightHighet = is_balance_and_high(node.right)
#             # right or left tree is not balanced, so the root is not balanced
#             if not leftValue or not rightValue:
#                 return False, max(leftHighet, rightHighet) + 1
#             # right and left are balanced but the height difference of them are bigger than 1
#             if abs(leftHighet - rightHighet) > 1:
#                 return False, max(leftHighet, rightHighet) + 1
#             return True, max(leftHighet, rightHighet) + 1
#
#         x, y = is_balance_and_high(root)
#         return x

import collections
q= collections.deque([(0,1,i) for i in range(4)])

q.append((1,2,3))
print(q)
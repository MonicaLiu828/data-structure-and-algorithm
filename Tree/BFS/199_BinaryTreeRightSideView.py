# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stor = deque([root])
        # stor.append(root)
        while stor:
            currentlen = len(stor)
            res.append(stor[-1].val)
            # count the times of currentlen(currentlenght is number of all element's at the same level)
            # when go outside of this loop, all element at the same level, so can go back line 15
            #  the last element is the rightest element at the current same level
            for i in range (currentlen):
                leftnode = stor.popleft()
                l = leftnode.left
                r = leftnode.right
                if l:
                    stor.append(l)
                if r:
                    stor.append(r)
        return res
# time O(n)
# space O(n/2) ->O(n)
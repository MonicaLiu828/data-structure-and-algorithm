# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        count = 0
        if not root:
            return []
        while queue:
            stor = []
            for i in range(len(queue)):
                left_node = queue.popleft()
                stor.append(left_node.val)
                if left_node.left:
                    queue.append(left_node.left)
                if left_node.right:
                    queue.append(left_node.right)
            if count % 2 == 0:
                res.append(stor)
                count += 1
            elif count % 2 ==1:
                stor.reverse()
                res.append(stor)
                count += 1
        print(res)
        return res

    # time: O(n)+logn/2 * O(n) -> nlogn
    # space: O(n) + O(n) -> O(n)
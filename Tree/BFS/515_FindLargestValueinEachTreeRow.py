# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            queue_len = len(queue)
            max = queue[0].val
            # loop each level of tree node, set original max = first element
            for i in range(queue_len):
                # from left to right to pop up each level element, and push its childeren into queue
                left_node = queue.popleft()
                if left_node.left:
                    queue.append(left_node.left)
                if left_node.right:
                    queue.append(left_node.right)
                if left_node.val > max:
                    max = left_node.val
            res.append(max)
        return res

    # time: O(n)
    # space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dict = {}

        def helper(root, depth):
            if not root:
                return
            if depth not in dict:
                dict[depth] = root.val
            elif depth in dict:
                dict[depth] = dict[depth] + root.val
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        arr = list(dict.keys())
        arr.sort()
        return dict[arr[-1]]
    # time: O(n) + nlogn
    # space: O(n)

    #     queue = deque()
    #     queue.append(root)
    #     # define a count without given a value at first
    #     count = None
    #     while queue:
    #         # return each level's element's count
    #         len_level = len(queue)
    #         # since leaf level after it's iterate, queue has been None, so
    #         # it will not go into this while loop, so at that time count should be right
    #         #  if there is a none leaf level, it will go back into this queue and count will be reset to 0
    #         count = 0
    #         for i in range (len_level):
    #             left_node = queue.popleft()
    #             # at each level we get the sum of this level
    #             count = count + left_node.val
    #             if left_node.left:
    #                 queue.append(left_node.left)
    #             if left_node.right:
    #                 queue.append(left_node.right)
    #     return count

    # # time: o(n)
    # # space: O(n)


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_subarr = []
        max_product = 0

        def sum_tree(node: [TreeNode]) -> int:
            if not node:
                sum_subarr.append(0)
                return 0
            # if not node.left and not node.right:
            #     sum_subarr.append(node.val)
            #     return node.val
            left_sum = sum_tree(node.left)
            right_sum = sum_tree(node.right)
            sum_subarr.append(left_sum + node.val + right_sum)
            return left_sum + node.val + right_sum

        total = sum_tree(root)
        # print(sum_subarr)
        for item in sum_subarr:
            if (total - item) * item > max_product:
                max_product = (total - item) * item
        return max_product % (10 ** 9 + 7)
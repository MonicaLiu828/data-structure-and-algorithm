class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        stor = []

        def helper(arr):
            if len(arr) == 1 or arr == []:
                return True
            l = 0
            r = len(arr) - 1
            while l <= r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1
            return True


        while queue:
            count = len(queue)
            stor = []
            for _ in range(count):
                popNode = queue.popleft()
                if popNode == None:
                    stor.append(None)
                else:
                    stor.append(popNode.val)
                    queue.append(popNode.left)
                    queue.append(popNode.right)
            if not helper(stor):
                return False
        return True
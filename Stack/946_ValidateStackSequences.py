class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while i < len(popped):
                if stack and stack[-1] == popped[i]:
                    stack.pop()
                    i += 1
                else:
                    break
        if len(stack) == 0:
            return True
        else:
            return False

        # time: O(2n)
        #  should be the length of pushed +popped but pushed = popped
        # space: O(n)
        #  n is the length of pushed

        # item_idx_map = dict()
        # for i in range(len(popped)):
        #     item_idx_map[popped[i]] = i
        # #  4-> 0 , 3-> 1
        # for i in range(len(pushed)-1):
        #     if pushed[i] != popped[0] and pushed[i+1] != popped[0]:
        #         if item_idx_map[pushed[i]] <  item_idx_map[pushed[i+1]]:
        #             return False


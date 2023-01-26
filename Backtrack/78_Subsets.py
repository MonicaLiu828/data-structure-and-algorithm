class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use index to make each number can only go to one bigger number instead of going back to smaller number
        res = []

        def backtrack(arr, index):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            res.append(arr[:])
            for index in range(index, len(nums)):
                arr.append(nums[index])
                index += 1
                backtrack(arr, index)
                # 'index -=1' can add but it does not have effect
                # since this for loop will go from prvious index +1, so this one does not have any effect
                arr.pop()

        backtrack([], 0)

        return res

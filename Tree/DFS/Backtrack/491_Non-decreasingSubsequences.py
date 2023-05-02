class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        stor = set()
        def dfs(arr, start):
            if len(arr) >= 2:
                if tuple(arr) not in stor:
                    stor.add(tuple(arr))
                    res.append(arr.copy())
            for i in range(start,len(nums)):
                if arr and nums[i] >= arr[-1]:
                    arr.append(nums[i])
                    dfs(arr,i+1)
                    arr.pop()
                elif not arr:
                    arr.append(nums[i])
                    dfs(arr,i+1)
                    arr.pop()
        dfs([],0)

        return res




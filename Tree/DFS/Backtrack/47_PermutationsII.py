class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        total_len = len(nums)
        res = []
        visited = [False] * total_len

        def dfs(curr_arr, visited):
            if len(curr_arr) == total_len:
                res.append(list(curr_arr))
                return
            for i in range(total_len):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                curr_arr.append(nums[i])
                dfs(curr_arr, visited)
                visited[i] = False
                curr_arr.pop()

        for i in range(total_len):
            dfs([], visited)
            return res
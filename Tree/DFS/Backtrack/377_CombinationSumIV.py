class Solution:
    def combinationSum4(self, candidates: List[int], target: int) -> int:
        res = []
        # candidates.sort()
        visited = [False] * len(candidates)

        def dfs(visited, start, curr_arr, num):
            if num == 0:
                res.append(list(curr_arr))
                print(curr_arr)
                return
            if num < 0:
                return
            for i in range(0, len(candidates)):
                # if i > 0 and candidates[i] == candidates[i-1] and not visited[i-1]:
                #     continue
                # visited[i] = True
                curr_arr.append(candidates[i])
                num -= candidates[i]
                dfs(visited, i, list(curr_arr), num)
                # visited[i] = False
                curr_arr.pop()
                num += candidates[i]

        dfs(visited, 0, [], target)
        return len(res)
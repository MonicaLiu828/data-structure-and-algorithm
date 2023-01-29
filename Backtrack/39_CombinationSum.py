# Solution 1:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums,count):
            if count == target:
                copy = nums[:]
                copy.sort()
                for item in res:
                    if len(item) == len(copy):
                        item.sort()
                        if item == copy:
                            return
                res.append(nums[:])
                return
            if count > target:
                return
            for item in candidates:
                nums.append(item)
                count = count + item
                backtrack(nums,count)
                nums.pop()
                count = count - item
        backtrack([],0)
        return res

# Solution 2:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums,count,start):
            if count == target:
                res.append(nums[:])
                return
            if count > target:
                return
            for i in range(start,len(candidates)):
                item = candidates[i]
                nums.append(item)
                count = count + item
                backtrack(nums,count,i)
                nums.pop()
                count = count - item
        backtrack([],0,0)
        return res
    # time: O(Npower(t/m+1))-> N is the length of candidates, t is target number, m is the minimum number of candidates' list
    # space:O(T/M)
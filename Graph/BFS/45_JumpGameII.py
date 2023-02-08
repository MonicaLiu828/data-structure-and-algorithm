class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        stor = deque()
        stor.append((0,nums[0],0))
        step = float('inf')
        seen = set()
        seen.add(0)
        while stor:
            i, k,s = stor.popleft()
            if i == len(nums)-1:
                return min(step,s)
            for j in range(0,k+1):
                newk = i+j
                news = s+1
                if newk < len(nums) and newk not in seen:
                    seen.add(newk)
                    stor.append((newk,nums[newk],news))



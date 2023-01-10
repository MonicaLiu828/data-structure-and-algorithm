class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # solution 1:
        # sort nums
        # find largest count number where sum number <= each query[i]
        # res = []
        # nums.sort()
        # for item in queries:
        #     sum = 0
        #     for i in range(len(nums)):
        #         if sum <= item:
        #             sum = sum+nums[i]
        #         if sum > item:
        #             break
        #         i+=1
        #     res.append(i)
        # return res

        # time: nlogn + m(O(n))
        # space: O1

        # soultion 2:
        # accumulate nums[i] and find last nums[i] < queries[i]
        res = []
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        for item in queries:
            l = 0
            r = len(nums)
            while l < r:
                m = (l+r)//2
                if nums[m] <= item:
                    l = m +1
                else:
                    r = m
            if m == nums[0] and nums[0] > item:
                res.append[0]
            res.append(r)
        return res

        # time: nlogn + +O(n) + m(logn)
        # space: O1

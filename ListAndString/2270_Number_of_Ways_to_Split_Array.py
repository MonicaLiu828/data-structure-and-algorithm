class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # get prefix of each nums
        # loop each prefix and get last prefix - curr prefix
        # compare with these two number
        count = 0
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        for j in range(len(prefix)-1):
            if prefix[j] >= prefix[-1]-prefix[j]:
                count +=1
        return count

    # time O（n)
    # space O(n)
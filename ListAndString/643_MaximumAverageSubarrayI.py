class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        arr = []
        for i in range(k):
            arr.append(nums[i])
            sum = sum + nums[i]
        ave = sum/k
        for i in range(k,len(nums)):
            arr.append(nums[i])
            original = arr[i-k]
            # arr = arr[1:len(arr)]
            sum = sum + nums[i]-original
            ave = max(ave,sum/k)
        return ave

    # time: O(n)
    # Space:O(1)
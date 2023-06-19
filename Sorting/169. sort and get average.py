class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums = sorted(nums, key=lambda c: c)
        nums.sort(key=lambda c: c)
        print(nums)
        ave = len(nums) // 2
        return nums[ave]

        # time: nlogn space: 1




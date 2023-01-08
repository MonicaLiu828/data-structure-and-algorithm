class Solution:

    # sliding window
    # deque
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        answer =0
        increase = deque()
        decrease = deque()
        for right,num in enumerate(nums):
            while increase and increase[-1] > num:
                increase.pop()
            increase.append(num)
            while decrease and decrease[-1] < num:
                decrease.pop()
            decrease.append(num)

            while increase and decrease and decrease[0] - increase[0] > limit:
                if increase[0] == nums[left]:
                    increase.popleft()
                if decrease[0] == nums[left]:
                    decrease.popleft()
                left += 1
            answer = max(right-left+1,answer)
        return answer
#   time : O(3n) -> o(n)
#   space: O(2n) -> o(n)

# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# solutions/609708/python-clean-monotonic-queue-solution-with-detail-explanation-o-n/




class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix_sum_arr = [0]
        for i in range(len(s)):
            prefix_sum_arr.append(prefix_sum_arr[-1] + int(s[i]))
        prefix_sum_arr = prefix_sum_arr[1:]

        total = prefix_sum_arr[-1]
        # all are zero to one
        flip = min(len(s) - total, total)

        for i in range(len(prefix_sum_arr)):
            left_one_total = prefix_sum_arr[i]
            right_zero_total = len(s) - i - 1 - (total - prefix_sum_arr[i])
            flip = min(flip, left_one_total + right_zero_total)
        return flip


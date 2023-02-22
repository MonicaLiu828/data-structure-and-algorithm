class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        idx_length_map = defaultdict(int)

        def helperfunc(left,right):
            if left == right:
                return 1
            if left > right:
                return 0
            if (left, right) in idx_length_map:
                return idx_length_map[(left, right)]
            length1 = 0
            if s[left] == s[right]:
                length1 = 2 + helperfunc(left + 1, right - 1)
                idx_length_map[(left,right)] = length1
                return length1
            length2 = helperfunc(left + 1, right)
            length3 = helperfunc(left, right - 1)
            maxlength = max(length1, length2, length3)
            idx_length_map[(left,right)] = maxlength
            return maxlength
        return helperfunc(0, len(s)-1)

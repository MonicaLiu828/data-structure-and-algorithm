class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def get_palindrom_from(s, left, right):
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return (right - left - 1, left + 1)
        # if not s:
        #     return ""
        # # (length,start)
        # answer = (0, 0)
        # for mid in range(len(s)):
        #     answer = max(answer, get_palindrom_from(s, mid, mid))
        #     answer = max(answer, get_palindrom_from(s, mid, mid + 1))

        # return s[answer[1]: answer[0] + answer[1]]

        if not s:
            return ''

        def is_palindrom(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            #  return length and start
            return (right - left - 1, left + 1)

        ans = (0, 0)
        for mid in range(len(s)):
            ans = max(ans, is_palindrom(mid, mid))
            ans = max(ans, is_palindrom(mid, mid + 1))

        return s[ans[1]: ans[1] + ans[0]]






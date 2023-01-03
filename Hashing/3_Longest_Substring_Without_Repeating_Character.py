# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        num = 0
        dict = defaultdict(int)
        for right in range(len(s)):
            if s[right] not in dict:
                dict[s[right]] = right+1
            else:
                # while s[left] != s[right]:
                #     del dict[s[left]]
                #     left += 1
                # left += 1
                left = max(left,dict.get(s[right]))
                dict[s[right]] = right+1
            num = max (num, right -left+1)
        return num
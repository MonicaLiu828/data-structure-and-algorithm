class Solution:
    def customSortString(self, order: str, s: str) -> str:
        word_idx_map = dict()
        for i in range(len(order)):
            word_idx_map[order[i]] = i
        res = ''
        for j in range(len(s)):
            if s[j] not in word_idx_map:
                res += s[j]
            elif len(res) == 0:
                res += s[j]
            else:

                i = 0
                while i < len(res):
                    if res[i] in word_idx_map and word_idx_map[res[i]] > word_idx_map[s[j]]:
                        res = res[:i] + s[j] + res[i:]
                        break

                    i += 1
                if i == len(res):
                    res = res + s[j]
        return res
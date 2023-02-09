class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        i,j = 0,0
        storP = defaultdict(int)
        for item in p:
            storP[item] += 1
        storRes = defaultdict(int)
        while j < len(s):
            storRes[s[j]] +=1
            count = j- i
            while storRes[s[j]] > storP[s[j]] or count > len(p)-1:
                storRes[s[i]] -= 1
                count -= 1
                i += 1
            if count == len(p)-1:
                newCount = True
                for key in storRes:
                    if storRes[key] != storP[key]:
                        newCount = False
                        break
                if newCount:
                    res.append(i)
            j += 1
        return res

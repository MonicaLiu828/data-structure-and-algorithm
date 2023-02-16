class Solution:
    def frequencySort(self, s: str) -> str:
        stor = defaultdict(int)
        for item in s:
            stor[item] += 1
        resStr = ''
        # for item in s:
        #     if resStr == '':
        #         resStr += item
        #     else:
        #         j = 0
        #         while j < len(resStr):
        #             if stor[item] > stor[resStr[j]]:
        #                 resStr = resStr[:j] + item + resStr[j:]
        #                 break
        #             j += 1

        #         if j == len(resStr) and stor[resStr[j-1] ]>= stor[item]:
        #             resStr += item
        # return resStr

        #  build a new map store (freq -> [ lettera, letterb])
        freqWord = defaultdict(list)
        for key in stor:
            freqWord[stor[key]].append(key)
        all_high_to_low_freq = []
        for key in freqWord:
            all_high_to_low_freq.append(key)
        all_high_to_low_freq.sort()
        #  get a freq from high to low 's freqList
        all_high_to_low_freq.reverse()
        for count in all_high_to_low_freq:
            #  letterArr is the arr of [ lettera, letterb], each has same freq
            letterArr = freqWord[count]
            for eachletter in letterArr:
                resStr = resStr + eachletter * count
        return resStr





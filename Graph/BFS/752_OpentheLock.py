class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        stor = deque()
        stor.append(['0000',0])
        seen =set()
        seen.add('0000')
        if target == '0000':
            return 0
        if "0000" in deadends:
            return -1


        def neighbor(numStr):
            res = []
            for i in range(4):
                for number in [-1,1]:
                    final = ''
                    converNum = int(numStr[i])+number
                    final = str(converNum%10)
                    convertedStr = numStr[:i]+ final+numStr[i+1:]
                    res.append(convertedStr)
            return res
        while stor:
            numStr,step = stor.popleft()
            if numStr == target:
               return step
            if numStr in deadends:
                continue
            for convertedStr in neighbor(numStr):
                    if convertedStr not in seen:
                        seen.add(convertedStr)
                        stor.append([convertedStr,step+1])
        return -1

    #   time:o(n) n is the length of deadends
    #   space: O(n) n is the length of deadends
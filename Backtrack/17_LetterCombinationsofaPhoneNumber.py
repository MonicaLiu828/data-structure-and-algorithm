class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def backtrack(currStr,i):
            if i == len(digits) and len(currStr)==len(digits) and len(digits) != 0:
                res.append(currStr)
                return
            elif len(digits) == 0:
                return res
            for i in range(i,len(digits)):
                if digits[i] in map:
                    for singleLetter in map[digits[i]]:
                        currStr+=singleLetter
                        backtrack(currStr,i+1)
                        currStr = currStr[:-1]
        backtrack('',0)
        return res

    #  time: 4powern(each max value in hashmap: 'wxyz')
    # space: O(N) -> recursion stack, since map is stable not change with input n, so it's O(1)-> total O(N)

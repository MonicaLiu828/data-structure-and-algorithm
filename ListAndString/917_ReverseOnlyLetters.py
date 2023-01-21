class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        newArr = list(s)
        i = 0
        j = len(newArr) - 1
        while i < j:
            if newArr[j].isalpha() and newArr[i].isalpha():
                stor = newArr[j]
                newArr[j] = newArr[i]
                newArr[i] = stor
                j -= 1
                i += 1
            elif newArr[j].isalpha() and not newArr[i].isalpha():
                i += 1
            else:
                j -= 1
        final = ''.join(newArr)
        return final





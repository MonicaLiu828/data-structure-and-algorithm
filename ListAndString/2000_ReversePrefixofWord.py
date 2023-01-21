class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        newArr = list(word)
        count = 0
        if ch in newArr:
            for i in range(len(newArr)):
                if newArr[i] == ch:
                    count = i
                    print(count)
                    break
            newStr = word[count::-1]
            print(newStr)
            newStr2 = word[count+1:]
            finalStr = newStr+newStr2
            return finalStr
        else:
            return word
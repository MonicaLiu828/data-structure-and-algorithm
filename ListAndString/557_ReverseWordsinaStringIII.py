class Solution:
    def reverseWords(self, s: str) -> str:
        newArr = s.split(' ')
        for i in range(len(newArr)):
            newArr[i] = newArr[i][::-1]
            # print(item)
        print(newArr)
        final = ' '.join(newArr)
        return final

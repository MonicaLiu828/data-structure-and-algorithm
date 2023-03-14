class Solution:
    def reverse(self, x: int) -> int:
        numStr = str(x)
        numArr =[]
        if numStr[-1] ==0:
            numStr = numStr[0:len(numStr)-1]
        for i in range(len(numStr)-1,-1,-1):
            numArr.append(numStr[i])
        res = ''
        for item in numArr:
            res += str(item)
        if res[-1] == '-':
            res = res[0:-1]
            if -int(res) < pow(-2,31):
                return 0
            else:
                return -int(res)
        if int(res) > pow(2,31):
            return 0
        else:
            return int(res)



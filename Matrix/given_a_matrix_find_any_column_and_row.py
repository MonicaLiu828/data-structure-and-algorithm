matrix = [['a','b','c'],['d','D','e'],['h','i','j'],['o','p','q']]
n=4
m=3
count=3
string1='abc'
string2='ad'
string3='sss'
def matrixfound(matrix,n,m,count,string1,string2,string3):
    stor_arr = []
    res = []
    for i in range(n):
        str = ''
        for j in range(m):
           str=str+matrix[i][j]
        stor_arr.append(str)

    for k in range(m):
        str = ''
        for h in range(n):
            str=str+matrix[h][k]
        stor_arr.append(str)

    def check(string):
        for item in stor_arr:
            if string == item or item.startswith(string):
                res.append(True)
                return
        res.append(False)
    check(string1)
    check(string2)
    check(string3)
    return res
print(matrixfound(matrix,n,m,count,string1,string2,string3))
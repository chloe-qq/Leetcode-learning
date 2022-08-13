"""
Microsoft 8/12笔试第二题

A = [1,4,4] 代表分母
B = [3,6,12]代表分母

查找分子/分母（对应位置） 之和= 1 的数量， 最后厨艺magic_number

float存储是有误差的！所以不能用A B对应相除然后用1减！
要存一个tuple 的形式！
"""
# default x < y
magic_number = 1
def gcd(x,y):
    #辗转相除法
    while(y):
        x, y = y, x%y
    return x
import math
def simplify(frac):
    x,y = frac
    z = gcd(x,y)
    z = math.gcd(x,y)
    return (x//z, y//z)
def findSum1Count(A,B):
    ans, n, frac2num = 0, len(A), {}
    
    for i in range(n):
        x, y = A[i], B[i]
        if (x > y):
            continue
        frac = simplify((x,y))
        targetFrac = simplify((y-x,y))
        
        if (targetFrac in frac2num):
            ans = (ans + frac2num[targetFrac])
        
        frac2num[frac] = frac2num.get(frac,0) + 1
    print(ans)
    return ans

A = [1,4,4] 
B = [3,6,12]
findSum1Count(A,B)
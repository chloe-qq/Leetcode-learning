"""
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

"""

def lc_substring(text1:str, text2:str)->str:
    # by default N1 < N2
    N1 = len(text1)
    N2 = len(text2)
    max_length = 0
    begin_index = -1
    dp = [ [0]*(N1+1) for _ in range(N2+1) ]
    for i2 in range(1,N2+1):
        for i1 in range(1,N1+1):
            if (text1[i1-1]==text2[i2-1]):
                dp[i2][i1] = dp[i2-1][i1-1] + 1
                if (dp[i2][i1] > max_length):
                    max_length = dp[i2][i1]
                    begin_index = i1-max_length
                elif (dp[i2][i1] == max_length):
                    begin_index = min(begin_index,i1-max_length)
            else:
                dp[i2][i1] = 0
    return text1[begin_index: begin_index + max_length]

text1 = "abdc"
text2 = "dccdab"
N1 = len(text1)
N2 = len(text2)
# 确保在短string 先出现的最为返回值
if (N1 < N2):
    print(lc_substring(text1,text2))
else:
    print(lc_substring(text2,text1))
"""
给定一个字符串，从左往右扫描，如存在两个或两个以上的相同字符靠在一起，则消除这些字符。对每次消除后剩下的字符，继续应用上述规则，直到不能再消除为止。
示例：
输入: abccbd 返回: ad 消除: cc、bb

输入: snggnngp 返回: sgp 消除: gg 、nnn

lc-1047

"""

def deleteNeightbourSame(text):
    stack = []
    char = ''

    for i in s:
        if (not stack):
            stack.append(i)
            continue
        if (stack and stack[-1] == i):
            stack.pop()
            if (len(stack) > 1 and stack[-1] == stack[-2]):
                stack.pop()
                stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)

text = 'snggnngp'
ans = deleteNeightbourSame(text)
print(ans)
            
            
"""
给定一个字符串，从左往右扫描，如存在两个或两个以上的相同字符靠在一起，则消除这些字符。对每次消除后剩下的字符，继续应用上述规则，直到不能再消除为止。
示例：
输入: abccbd 返回: ad 消除: cc、bb

输入: snggnngp 返回: sgp 消除: gg 、nnn

"""

def deleteNeightbourSame(text):
    stack = []
    char = ''
    isSame = False
    for c in text:        
        if (isSame):
            if (c == char):
                continue
            else:
                isSame = False
                char = ''
        # not isSame   
        if ((not stack) or c!=stack[-1]):
            stack.append(c)
        elif (stack and c==stack[-1]):
            char = stack.pop()
            isSame = True
    return ''.join(stack)

text = 'snggnngp'
ans = deleteNeightbourSame(text)
print(ans)
            
            
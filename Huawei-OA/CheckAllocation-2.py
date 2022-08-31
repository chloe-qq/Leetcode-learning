"""
给定字符串
S表示正常输入

#参考 四则运算 括号匹配问题


re.split()
re.split(pattern, string, maxsplit=0, flags=0)
pattern：
    相当于str.split()中的sep，分隔符的意思，
    不但可以是字符串，
    也可以为正则表达式: '[ab]'，表示的意思就是取a和b的任意一个值
    （可参考： https://docs.python.org/3/library/re.html?highlight=re%20split#re.split ）
string：要进行分割的字符串
maxsplit：分割的最大次数，这个参数和str.split()中有点不一样：
"""


import re
command = "S{{M0S}F0}F0"
# 1）去除字符串中的空格, 三种方法
command = command.replace(' ', '')
command = ''.join(command.split())

# use stack 括号匹配
def is_encode(command):
    # 放左右括号的栈
    bracket = '{}'
    open_brackets = []
    close_brackets = ['}']
    # 见一个右括号就出一个左括号
    for i in range(len(command)):
        char = command[i]
        # 如果不是括号，下一个
        if (bracket.find(command) == -1 or char == 'S'):
            continue
        # 如果是左括号就入栈
        if char == '{':
            open_brackets.append(si)
            continue
        # 走下下面说明就是右括号了，因为上面已经排除了不是字母和左括号了
        if len(open_brackets) == 0:
            # 现在来了个右括号，但是没有匹配的了
            return False
        #上面排除了各种情况，现在开始正常匹配了
        p = open_brackets.pop()
        if p =='(' and si ==')':
            continue
        else:
            return False

    #判断是否还有多余的左括号呀
    if len(open_brackets) > 0:
        return False
    return True
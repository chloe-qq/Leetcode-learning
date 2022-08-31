"""
给定一个只包含大写英文字母的字符串S，要求你给出对S重新排列的所有不相同的排列数。
如：S为ABA，则不同的排列有ABA、AAB、BAA三种。

"""

def permutation(s):
    ans = []
    N = len(s)
    hashmap = {}
    for char in s:
        hashmap[char] = hashmap.get(char,0) + 1

    def dfs(cur, hashmap):
        if (len(cur) == N):
            ans.append(cur)
            return
        
        for i in hashmap.keys():
            if (hashmap[i] > 0):
                cur += i
                hashmap[i] -= 1
                dfs(cur,hashmap)
                cur = cur[:-1]
                hashmap[i] += 1
                
    dfs('',hashmap)
    return ans
        
s = 'ABA'
ans = permutation(s)
print(ans)
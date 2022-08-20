"""
131. Palindrome Partitioning
Given a string s, 
partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]


"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPalidrome(left, right):
            if (left == right):
                return True
            while(left < right):
                if (s[left] == s[right]):
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        ans = []
        N = len(s)
        def dfs(i, cur):
            if (i == N):
                ans.append(cur.copy())
                return
            for j in range(i+1, N+1):
                # if is Palidrome, append to cur
                # and then start at the next position
                if (checkPalidrome(i,j-1)):
                    cur.append(s[i:j])
                    dfs(j,cur)
                    #backtrack
                    cur.pop()
                else:
                    
                    continue
        dfs(0,[])
        return ans
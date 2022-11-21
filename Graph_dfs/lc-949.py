class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        hashmap = Counter(arr)
        ans = []
        def checkvalid(cur):
            N = len(cur)
            if (N == 1):
                if (int(cur) >= 3):
                    return False
            elif (N == 2):
                if (int(cur) > 23):
                    return False
            elif (N == 3):
                if (int(cur[:2]) > 23 or int(cur[2]) >=6):
                    return False
            else:
                if (int(cur[:2]) > 23 or int(cur[2:]) >59):
                    return False
            return True

                    
        def dfs(cur, hashmap):
            if (len(cur) == 4):
                ans.append(cur)
                return
            for i in hashmap.keys():
                if (hashmap[i] > 0):
                    cur += str(i)
                    hashmap[i] -= 1
                    if (checkvalid(cur)):
                        dfs(cur,hashmap)                    
                    cur = cur[:-1]
                    hashmap[i] += 1
        dfs('',hashmap)
        if (ans == []):
            return ''
        maxTime = sorted(ans)[-1]
        hour = ''.join(maxTime[:2])
        minute = ''.join(maxTime[2:])
        return hour+':'+minute
        
                
                


            


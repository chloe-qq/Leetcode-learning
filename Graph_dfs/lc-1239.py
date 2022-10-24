from collections import Counter
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        def dfs(currMap, idx):
            # check the current combination valid or not
            if (len(currMap) > 0 and Counter(currMap).most_common(1)[0][1] > 1):
                return 0

            best = len(currMap)
            
            for i in range(idx, N):
                wordMap = Counter(arr[i])
                if (len(wordMap) > len(arr[i])):
                    # current word has duplicate
                    continue
                
                currMap.update(wordMap)
                best = max(best, dfs(currMap, i+1))
                # backtrack
                for c in wordMap:
                    if (currMap[c] == wordMap[c]):
                        del currMap[c]
                    else:
                        currMap[c] -= wordMap[c]
            return best
        return dfs(Counter(),0)
                
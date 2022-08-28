
from typing import List
from collections import defaultdict,deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        queue = deque(supplies)
        preCount = defaultdict(int)        
        prepare = defaultdict(list)
        ans = []
        for i,ing in enumerate(ingredients):
            for j in ing:
                prepare[j].append(recipes[i])
                preCount[recipes[i]] += 1

        while queue:
            cur = queue.popleft()
            for j in prepare[cur]:
                preCount[j] -= 1
                if (preCount[j] == 0):
                    queue.append(j)
                    if j in recipes:
                        ans.append(j)
        return ans
                    
                    
                    
                    
                
                
                
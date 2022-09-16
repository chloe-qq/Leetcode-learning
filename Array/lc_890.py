class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m1, m2 = {},{}
            
            for w,p in zip(word,pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if (p,w) != (m1[w], m2[p]):

                    return False
            return True
        #  filter() function extracts elements from an iterable (list, tuple etc) for which a function returns True
        
                
        return filter(match, words)
                
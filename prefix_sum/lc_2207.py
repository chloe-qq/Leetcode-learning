class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # count the appear time of pattern[1] for each index
        N = len(text)
        appear_pattern1 = [0]*N
        appear_pattern1[N-1] = 1 if text[-1] == pattern[1] else 0
        appear_pattern0 = 1 if text[-1] == pattern[0] else 0
        for i in range(N-2,-1,-1):
            appear_pattern1[i] = appear_pattern1[i+1]+1 if text[i] == pattern[1] else appear_pattern1[i+1]
            appear_pattern0 += 1 if text[i] == pattern[0] else 0
        appear_cnt_max = max(appear_pattern0,appear_pattern1[0])


        ans = 0

        for i in range(N):
            if (text[i] == pattern[0]):
                ans += appear_pattern1[i]
                if (pattern[0] == pattern[1]):
                    # important!
                    ans -= 1
        return ans + appear_cnt_max
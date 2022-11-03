class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = collections.Counter(words)
        ans = 0
        distinctword = list(hashmap.keys())
        addedMiddle = False
        for word in distinctword:
            # 本身就是回文串
            if (word == word[::-1]):
                occ = hashmap[word]//2
                ans += occ*2*2
                if (addedMiddle == False and (hashmap[word]-2*occ == 1)):
                    ans += 2
                    addedMiddle = True
                    
                continue
            if (hashmap[word] > 0):
                # 可能和另一个字符串为回文串
                if (hashmap[word[::-1]] > 0):
                    min_freq = min(hashmap[word], hashmap[word[::-1]])
                    ans += 2*2*min_freq
                    hashmap[word] -= min_freq
                    hashmap[word[::-1]] -= min_freq
        return ans
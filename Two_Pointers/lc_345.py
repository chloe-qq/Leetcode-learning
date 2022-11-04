class Solution:
    def reverseVowels(self, s: str) -> str:
        text = list(s)
        left = 0
        right = len(text)-1
        vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        while (left < right):
            if (text[left] in vowels and text[right] in vowels):
                tmp = text[left]
                text[left] = text[right]
                text[right] = tmp
                left += 1
                right -= 1
                continue
            elif (text[left] not in vowels):
                left += 1
            elif (text[right] not in vowels):
                right -= 1
        return ''.join(text)


lc_345 = Solution()
s = "hello"
lc_345.reverseVowels(s)
        
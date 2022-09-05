"""
You can choose which characters each button is matched to as long as:
    All 26 lowercase English letters are mapped to.
    Each character is mapped to by exactly 1 button.
    Each button maps to at most 3 characters.

Solution Hint:
Map the most frequent letters so that you can type them with only 1 keypress.
Use an array to keep track of the frequency of every character, then sort it in non-increasing order.
"""

# python collections.Counter can count the word frequency
import collections
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        digit_dict = collections.Counter(s)
        ans = 0
        freq = sorted(digit_dict.values(), reverse = True)
        
        for i, cnt in enumerate(freq):
            press_cnt = i//9 + 1
            ans += cnt*press_cnt
        return ans
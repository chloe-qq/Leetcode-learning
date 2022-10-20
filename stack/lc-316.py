
import heapq
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        lastOccurance = {c:i for i,c in enumerate(s)}
        for i,char in enumerate(s):
            if char not in seen:
                # make sure increasing order
                while stack and char < stack[-1] and i < lastOccurance[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)
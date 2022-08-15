"""
first in last out problem --> consider stack

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        W = len(heights)
        maxArea = heights[0] * 1
        stack.append([0,heights[0]])
        for i in range(1,W):
            
            if (heights[i] < heights[i-1]):
                tempW = W
                while (stack and stack[-1][1] > heights[i]):
                    tempW = min(tempW,stack[-1][0])
                    # before pop out calculate the maxArea
                    maxArea = max(maxArea, stack[-1][1] * (i-stack[-1][0]))
                    stack.pop()
                # need to extend i back to the latest popped number's index because the current number can be left extended!!!
                stack.append([tempW, heights[i]])

            else:
                stack.append([i, heights[i]])

        if (stack):
            for i, hi in stack:
                maxArea = max(maxArea, (W-i)*hi)
        return maxArea
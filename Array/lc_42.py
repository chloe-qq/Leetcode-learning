"""
Tapping raining water
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        highest_index = -1
        highest = 0
        volume = 0
        
        for i, h in enumerate(height):
            if (h > highest):
                highest = h
                highest_index = i
        
        # find left highest
        left_highest = height[0]
        for i in range(highest_index+1):
            if (height[i] <  left_highest):
                volume += left_highest - height[i]
            else:
                left_highest = height[i]
     
        N = len(height)-1      
        right_highest = height[N]
        for i in range(N, highest_index-1, -1):
            if (height[i] < right_highest):
                volume +=   right_highest-height[i]
            else:
                right_highest = height[i]
        return volume      
                
                
                
        
                
        
    
    
lc_42 = Solution()
height = [3,1,2,5,2,4] 
print(lc_42.trap(height))
            
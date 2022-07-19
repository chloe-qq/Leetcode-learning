"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Input: s = "(*)"
Output: true

Input: s = "(*))"
Output: true

Solution:
[greedy] keep track of the maximum and minimum possibility of left '(' depend on the choice of *
if left is negative NOT due to the choice of '*', return False, as it will be kind of ))( 

can also be done by brute force (decision-tree) -->O(n^3)
"""

class Solution:
   def checkValidString(self, s: str) -> bool:      
      left_min = 0
      left_max = 0
      for c in s:
         if c == '(':
            left_min += 1
            left_max += 1
         elif c == ')':
            left_min -= 1
            left_max -= 1
            # since due to ) left_min < 0 is not possible
            left_min = max(0, left_min)
            if (left_max < 0):
               return False
         else:
            left_max += 1
            left_min -= 1
            left_min = max(0, left_min)
         print(f'left_min:{left_min}')
         print(f'left_max:{left_max}')
         print('------')
      return True if (left_min <=0 and left_max >= 0) else False
            
 
lc_678 = Solution()
s = "(*)((*"
print(lc_678.checkValidString(s))
           
                
               
               
   
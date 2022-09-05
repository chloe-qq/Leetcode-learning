class Solution:
    # 非常类似lc1249 two pass solution, lc-678的思路
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if ( N%2 == 1):
            return False

        max_balance = 0 # max left bracket can be used
        min_balance = 0 # min left bracket to be balanced
        left_bracket = '('
        for i in range(N):
            if (locked[i] == '1'):
                if (s[i] == left_bracket):
                    min_balance += 1
                    max_balance += 1
                else:
                    min_balance -= 1
                    max_balance -= 1
                    if (max_balance < 0):
                        return False    
                min_balance = max(0,min_balance)
            else:
                # locked[i] == '0'
                # can be either ( or ) 
                max_balance += 1
                min_balance -= 1
                min_balance = max(0,min_balance)
            #print(f'max_balance:{max_balance}, min_balance = {min_balance}')
        return True if (max_balance >=0 and min_balance <=0) else False
                
            
            
            
        
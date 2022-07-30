class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        
        for i in range(9):
            hashset.clear()
            for j in range(9):
                if (board[i][j] == '.'):
                    continue
                elif (board[i][j] in hashset):
                    print(f'i = {i}, j = {j},output-1 to False')
                    return False
                else:
                    hashset.add(board[i][j])
        for i in range(9):
            hashset.clear()
            for j in range(9):
                if (board[j][i] == '.'):
                    continue
                elif (board[j][i] in hashset):
                    print(f'i = {i}, j = {j},output-2 to False')
                    return False
                else:
                    hashset.add(board[j][i]) 
                    
        for k1 in range(3):
            for k2 in range(3):
                hashset.clear()
                for i in range(3):
                    for j in range(3):
                        if (board[k1*3+i][k2*3+j] == '.'):
                            continue
                        elif (board[k1*3+i][k2*3+j] in hashset):
                            print(f'i = {k1*3+i}, j = {k2*3+j},output-3 to False')
                            return False
                        else:
                            hashset.add(board[k1*3+i][k2*3+j])
        return True
                            
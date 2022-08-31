

def check_each(matrix, m, n, diff)->bool:
    if (diff >= 0):
        val = matrix[diff][0]
    else:
        val = matrix[0][-diff]
    for i in range(m):
        for j in range(n):
            if (i-j == diff):
                if (matrix[i][j] != val):
                    return False
    return True

def check(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for diff in range(-n+1+1, m-1, 1):
        if (not check_each(matrix, m,n, diff)):
            return False
    return True
                
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
#matrix = [[1,2],[2,2]]
print(check(matrix))
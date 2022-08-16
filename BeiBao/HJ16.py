
# https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 华为机试 牛客HJ16
N,m = map(int,input().split(' '))
main_component = {}
affli_component = {}
item_index = 1
while True:
    try:
        value, importance, q = map(int,input().split(' ')) 
        if (q == 0):
            main_component[item_index] = [value, importance]
        else:
            affli_component[q] = affli_component.get(q,[]) + [[value,importance]]
        item_index += 1
    except EOFError:
        break

main_cnt = len(main_component)
Value_vector = []
Importance_vector = []
# main_component, 
# main_component + affli_1 ,  main_component + affli_2
# main_component + affli_1 + affli2

for i in main_component.keys():
    V_temp,I_temp = [],[]
    V_temp.append(main_component[i][0])
    I_temp.append(main_component[i][0]*main_component[i][1])
    if (i in affli_component.keys()):
        V_temp.append(V_temp[0]+affli_component[i][0][0])# 主+附1
        I_temp.append(I_temp[0]+affli_component[i][0][0]*affli_component[i][0][1])
        if (len(affli_component[i])>1):
            V_temp.append(V_temp[0]+affli_component[i][1][0])# 主+附2
            I_temp.append(I_temp[0]+affli_component[i][1][0]*affli_component[i][1][1])
            
            V_temp.append(V_temp[1]+affli_component[i][1][0])# 主+附1+附2
            I_temp.append(I_temp[1]+affli_component[i][1][0]*affli_component[i][1][1])
    Value_vector.append(V_temp)
    Importance_vector.append(I_temp)
dp = [[0]*(N+1) for _ in range(main_cnt+1)]

for i in range(1,main_cnt+1):
    for j in range(10, N+1,10): #物品的价格是10的整数倍
        cur_max = dp[i-1][j]
        
        for k in range(len(Value_vector[i-1])):
            if (j - Value_vector[i-1][k] >= 0):
                cur_max = max(cur_max,dp[i-1][j-Value_vector[i-1][k]]+Importance_vector[i-1][k])
        dp[i][j] = cur_max
print(dp[-1][-1])
            
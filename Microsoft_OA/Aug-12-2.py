"""
Microsoft 8/12笔试第3题

event = [2,3,7,2,1,4]
x: 参加几场event
y: 每场event之间需要有几次空隙
event为每个event 需要花费的cost
问：最小的cost
guarantee (x-1)*y <= len(event)

"""

def getsubseq(event, y):
    candidates = []
    for i in range(y):
        candidates.append([event[i] for i in range(i,len(event),y)])
    return candidates

def find_Opt_k(array, k):

    subSum, i, arrayLen = sum(array[:k]),k,len(array)
    min_cost = subSum

    for i in range(k, arrayLen):
        subSum += array[i] - array[i-k]
        min_cost = min(min_cost,subSum)
    return min_cost
        

def findMinCost(event, x,y):
    candidates = getsubseq(event,y)


    min_cost = float('inf')
    for i in range(y):
        min_cost = min(find_Opt_k(candidates[i], x),min_cost )
        
    print(min_cost)    
    return min_cost
    
event = [2,3,7,9,1,4,3,2,1,4,5,9]
x = 2
y = 3
findMinCost(event, x, y)
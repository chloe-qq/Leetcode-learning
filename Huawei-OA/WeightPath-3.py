"""
行军路线，经过不同节点（只可走一次），有gain(正数) or cost（负数）
从Start开始走，走到End结束，问 最 大 化收益

dijkstra 算法 + 贪心
求的那个东西其实等价于是带权重的有向图的最短路径

因为只有最小堆，所以要改成负数 cost 就是正； gain就为负数， heap每次取min出来（也就是gain最大的），取出来之后需要取反
当取出来发现visited[node] != weight, 说明此点已经被更新过了，不需要再更新一遍了

判断的时候 当某个点已经被visit 也要继续判断现在的路径是否比原来的路径大

graph存储形式是dict{dict}
{start:{a:-22, b:-30}, a:{c,-12} ...}
"""


from collections import defaultdict
import heapq


input_graph = [
    ['Start','A',-22],
    ['Start','B',-30],
    ['B','A',12],
    ['A','C',-30],
    ['C','D',-15],
    ['C','E',15],
    ['E','F',22],
    ['D','End',-21],
    ['E','End',-32]  
]


def maxGain(s,end):
    graph = defaultdict(dict)
    
    for v1, v2, cost in input_graph:
        graph[v1][v2] = cost
    print(graph)
    
    # set start point
    visited = {s:0} 
    
    # use min heap to optimize
    heap = [(0,s)]
    
    while (heap):
        weight, node = heapq.heappop(heap)
        # revsrse weight due to we want to calculate max, but we only have min heap
        # so when we put value in heap, we actually put the negative one into it
        weight = -weight
        if (node not in graph):
            continue
        
        # because
        if (visited[node] != weight):
            print('visited[node] != weight')
        
        for next_node, next_weight in graph[node].items():
            if (next_node not in visited or (next_node in visited and visited[next_node] < weight + next_weight)):
                visited[next_node] = weight + next_weight
                heapq.heappush(heap, (-visited[next_node], next_node))
    return visited[end]
        
        
    
print(maxGain('Start','End')+1e6)
